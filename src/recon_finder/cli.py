from __future__ import annotations

import argparse
from pathlib import Path
from urllib.parse import urlparse

from rich.console import Console
from rich.table import Table

from . import __version__
from .scanner import Scanner


console = Console()


def normalize_target(target: str) -> str:
    """Normalize and validate a target URL."""

    target = target.strip()

    if not target.startswith(("http://", "https://")):
        target = f"https://{target}"

    parsed = urlparse(target)

    if not parsed.netloc:
        raise ValueError("Invalid target URL.")

    return target


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="recon-finder",
        description="Simple HTTP reconnaissance file discovery tool.",
    )

    parser.add_argument(
        "target",
        help="Target URL, e.g. https://example.com",
    )

    parser.add_argument(
        "-w",
        "--wordlist",
        type=Path,
        default=Path("wordlists/common.txt"),
        help="Path to discovery wordlist.",
    )

    parser.add_argument(
        "-t",
        "--timeout",
        type=float,
        default=5.0,
        help="HTTP timeout in seconds.",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    return parser


def print_result(result) -> None:
    if result.error:
        console.print(
            f"[red][ERR][/red] {result.url} — {result.error}"
        )
        return

    status = result.status_code

    if status == 200:
        style = "green"
    elif status in {301, 302, 307, 308}:
        style = "yellow"
    elif status in {401, 403}:
        style = "magenta"
    elif status == 404:
        style = "dim"
    else:
        style = "cyan"

    console.print(
        f"[{style}][{status}][/{style}] "
        f"{result.url} "
        f"[dim]({result.content_length} bytes, "
        f"{result.elapsed:.2f}s)[/dim]"
    )


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    try:
        target = normalize_target(args.target)
    except ValueError as exc:
        parser.error(str(exc))

    if not args.wordlist.exists():
        parser.error(f"Wordlist not found: {args.wordlist}")

    scanner = Scanner(
        target=target,
        timeout=args.timeout,
    )

    console.print()
    console.print(
        f"[bold]RECON-FINDER[/bold] "
        f"[dim]v{__version__}[/dim]"
    )
    console.print(f"Target: [cyan]{target}[/cyan]")
    console.print(f"Wordlist: [cyan]{args.wordlist}[/cyan]")
    console.print()

    results = []

    for result in scanner.scan_wordlist(args.wordlist):
        results.append(result)

        if result.found:
            print_result(result)

    found = sum(result.found for result in results)
    errors = sum(result.error is not None for result in results)

    console.print()

    table = Table(title="Scan Summary")

    table.add_column("Requests")
    table.add_column("Found")
    table.add_column("Errors")

    table.add_row(
        str(len(results)),
        str(found),
        str(errors),
    )

    console.print(table)