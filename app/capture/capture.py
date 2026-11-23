"""Basic screen capture backed by MSS and OpenCV."""

from typing import Iterator, Optional

import numpy as np

from app.config import CaptureConfig


class FrameCapture:
    """Capture a configurable screen region as NumPy image frames."""

    def __init__(self, config: Optional[CaptureConfig] = None) -> None:
        self.config = config or CaptureConfig.from_env()
        if self.config.width <= 0 or self.config.height <= 0:
            raise ValueError("capture width and height must be positive")
        if self.config.top < 0 or self.config.left < 0:
            raise ValueError("capture top and left must be non-negative")

        try:
            import mss
        except ImportError as exc:
            raise RuntimeError("MSS is required for screen capture") from exc

        self._mss = mss.mss()
        self.region = {
            "top": self.config.top,
            "left": self.config.left,
            "width": self.config.width,
            "height": self.config.height,
        }

    def capture_frame(self) -> np.ndarray:
        """Capture and return one frame in BGR format."""
        screenshot = self._mss.grab(self.region)
        frame = np.asarray(screenshot, dtype=np.uint8)
        return frame[:, :, :3]

    def frames(self) -> Iterator[np.ndarray]:
        """Yield captured frames until the caller stops iteration."""
        while True:
            yield self.capture_frame()

    def close(self) -> None:
        """Release capture resources."""
        self._mss.close()
