"""Perception interfaces."""

from .interfaces import (
    Detection,
    ObjectDetector,
    PlaceholderObjectDetector,
    PlaceholderRoadSegmentation,
    RoadSegmentation,
    SegmentationMask,
)

__all__ = [
    "Detection",
    "ObjectDetector",
    "PlaceholderObjectDetector",
    "PlaceholderRoadSegmentation",
    "RoadSegmentation",
    "SegmentationMask",
]
