import numpy as np

from app.perception import PlaceholderObjectDetector, PlaceholderRoadSegmentation


def test_placeholder_object_detector_returns_no_detections() -> None:
    image = np.zeros((32, 32, 3), dtype=np.uint8)

    assert PlaceholderObjectDetector().detect(image) == ()


def test_placeholder_segmentation_returns_matching_mask() -> None:
    image = np.zeros((32, 48, 3), dtype=np.uint8)

    result = PlaceholderRoadSegmentation().segment(image)

    assert result.mask.shape == (32, 48)
