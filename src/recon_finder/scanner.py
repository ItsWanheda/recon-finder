from __future__ import annotations

from pathlib import Path
from typing import Iterator
from urllib.parse import urljoin

import requests

from .results import ScanResult


class Scanner:
    """HTTP path discovery scanner."""

    def __init__(
        self,
        target: str,
        timeout: float = 5.0,
        user_agent: str = "recon-finder/0.1.0",
    ) -> None:
        self.target = target.rstrip("/") + "/"
        self.timeout = timeout

        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": user_agent,
            }
        )

    def scan_path(self, path: str) -> ScanResult:
        """Scan a single path."""

        path = path.strip().lstrip("/")
        url = urljoin(self.target, path)

        try:
            response = self.session.get(
                url,
                timeout=self.timeout,
                allow_redirects=False,
            )

            return ScanResult(
                url=url,
                status_code=response.status_code,
                content_length=len(response.content),
                elapsed=response.elapsed.total_seconds(),
            )

        except requests.RequestException as exc:
            return ScanResult(
                url=url,
                status_code=None,
                content_length=0,
                elapsed=0.0,
                error=str(exc),
            )

    def scan_wordlist(self, wordlist: Path) -> Iterator[ScanResult]:
        """Scan every path in a wordlist."""

        with wordlist.open("r", encoding="utf-8") as file:
            for line in file:
                path = line.strip()

                if not path or path.startswith("#"):
                    continue

                yield self.scan_path(path)