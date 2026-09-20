from dataclasses import dataclass
from typing import Optional


@dataclass
class ScanResult:
    """Result of a single HTTP discovery request."""

    url: str
    status_code: Optional[int]
    content_length: int
    elapsed: float
    error: Optional[str] = None

    @property
    def found(self) -> bool:
        """Return True when the resource was successfully discovered."""
        return (
            self.error is None
            and self.status_code is not None
            and self.status_code not in {404}
        )