from pathlib import Path

import requests

from recon_finder.results import ScanResult
from recon_finder.scanner import Scanner


class FakeResponse:
    """Minimal fake response for scanner tests."""

    def __init__(
        self,
        status_code: int,
        content: bytes = b"",
        elapsed_seconds: float = 0.1,
    ) -> None:
        self.status_code = status_code
        self.content = content
        self.elapsed = type(
            "Elapsed",
            (),
            {"total_seconds": lambda self: elapsed_seconds},
        )()


def test_scanner_normalizes_target() -> None:
    scanner = Scanner("https://example.com")

    assert scanner.target == "https://example.com/"


def test_scan_path(monkeypatch) -> None:
    scanner = Scanner("https://example.com")

    def fake_get(*args, **kwargs):
        assert args[0] == "https://example.com/robots.txt"
        assert kwargs["timeout"] == 5.0
        assert kwargs["allow_redirects"] is False

        return FakeResponse(
            status_code=200,
            content=b"User-agent: *",
        )

    monkeypatch.setattr(scanner.session, "get", fake_get)

    result = scanner.scan_path("robots.txt")

    assert isinstance(result, ScanResult)
    assert result.url == "https://example.com/robots.txt"
    assert result.status_code == 200
    assert result.content_length == len(b"User-agent: *")
    assert result.error is None
    assert result.found is True


def test_scan_path_removes_leading_slash(monkeypatch) -> None:
    scanner = Scanner("https://example.com")

    requested_urls = []

    def fake_get(url, **kwargs):
        requested_urls.append(url)

        return FakeResponse(
            status_code=200,
            content=b"OK",
        )

    monkeypatch.setattr(scanner.session, "get", fake_get)

    scanner.scan_path("/admin/")

    assert requested_urls == [
        "https://example.com/admin/"
    ]


def test_scan_path_handles_404(monkeypatch) -> None:
    scanner = Scanner("https://example.com")

    def fake_get(*args, **kwargs):
        return FakeResponse(
            status_code=404,
            content=b"Not Found",
        )

    monkeypatch.setattr(scanner.session, "get", fake_get)

    result = scanner.scan_path("missing")

    assert result.status_code == 404
    assert result.content_length == len(b"Not Found")
    assert result.error is None
    assert result.found is False


def test_scan_path_handles_redirect(monkeypatch) -> None:
    scanner = Scanner("https://example.com")

    def fake_get(*args, **kwargs):
        return FakeResponse(
            status_code=301,
            content=b"",
        )

    monkeypatch.setattr(scanner.session, "get", fake_get)

    result = scanner.scan_path("admin")

    assert result.status_code == 301
    assert result.found is True


def test_scan_path_handles_forbidden(monkeypatch) -> None:
    scanner = Scanner("https://example.com")

    def fake_get(*args, **kwargs):
        return FakeResponse(
            status_code=403,
            content=b"Forbidden",
        )

    monkeypatch.setattr(scanner.session, "get", fake_get)

    result = scanner.scan_path(".env")

    assert result.status_code == 403
    assert result.found is True


def test_scan_path_handles_request_error(monkeypatch) -> None:
    scanner = Scanner("https://example.com")

    def fake_get(*args, **kwargs):
        raise requests.RequestException("Connection failed")

    monkeypatch.setattr(scanner.session, "get", fake_get)

    result = scanner.scan_path("admin")

    assert result.url == "https://example.com/admin"
    assert result.status_code is None
    assert result.content_length == 0
    assert result.error == "Connection failed"
    assert result.found is False


def test_scan_wordlist(tmp_path: Path, monkeypatch) -> None:
    scanner = Scanner("https://example.com")

    wordlist = tmp_path / "test.txt"

    wordlist.write_text(
        """
# Comment
admin

login
robots.txt
""",
        encoding="utf-8",
    )

    requested_paths = []

    def fake_scan_path(path):
        requested_paths.append(path)

        return ScanResult(
            url=f"https://example.com/{path}",
            status_code=200,
            content_length=10,
            elapsed=0.1,
        )

    monkeypatch.setattr(scanner, "scan_path", fake_scan_path)

    results = list(scanner.scan_wordlist(wordlist))

    assert requested_paths == [
        "admin",
        "login",
        "robots.txt",
    ]

    assert len(results) == 3
    assert all(result.found for result in results)

