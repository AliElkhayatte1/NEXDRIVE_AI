"""Environment-based application configuration."""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class CaptureConfig:
    """Configuration for a rectangular screen capture region."""

    top: int = 0
    left: int = 0
    width: int = 1920
    height: int = 1080

    @classmethod
    def from_env(cls) -> "CaptureConfig":
        """Load capture settings from environment variables."""
        return cls(
            top=int(os.getenv("NEXDRIVE_CAPTURE_TOP", "0")),
            left=int(os.getenv("NEXDRIVE_CAPTURE_LEFT", "0")),
            width=int(os.getenv("NEXDRIVE_CAPTURE_WIDTH", "1920")),
            height=int(os.getenv("NEXDRIVE_CAPTURE_HEIGHT", "1080")),
        )
