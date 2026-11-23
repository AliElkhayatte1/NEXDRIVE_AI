"""Placeholder interfaces for future perception implementations."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Sequence

import numpy as np


@dataclass(frozen=True)
class Detection:
    """A detected object and its confidence."""

    label: str
    confidence: float
    bounding_box: tuple[int, int, int, int]


@dataclass(frozen=True)
class SegmentationMask:
    """A road segmentation mask returned by a future model."""

    mask: np.ndarray


class ObjectDetector(ABC):
    """Interface for object detection models."""

    @abstractmethod
    def detect(self, image: np.ndarray) -> Sequence[Detection]:
        """Detect objects in an image."""
        raise NotImplementedError


class RoadSegmentation(ABC):
    """Interface for road or drivable-area segmentation models."""

    @abstractmethod
    def segment(self, image: np.ndarray) -> SegmentationMask:
        """Return a segmentation mask for an image."""
        raise NotImplementedError


class PlaceholderObjectDetector(ObjectDetector):
    """Explicitly non-functional object detector for interface testing."""

    def detect(self, image: np.ndarray) -> Sequence[Detection]:
        if not isinstance(image, np.ndarray):
            raise TypeError("image must be a NumPy array")
        return ()


class PlaceholderRoadSegmentation(RoadSegmentation):
    """Explicitly non-functional segmentation implementation."""

    def segment(self, image: np.ndarray) -> SegmentationMask:
        if not isinstance(image, np.ndarray):
            raise TypeError("image must be a NumPy array")
        return SegmentationMask(mask=np.zeros(image.shape[:2], dtype=np.uint8))
