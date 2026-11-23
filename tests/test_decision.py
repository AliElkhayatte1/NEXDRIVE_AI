import numpy as np
import pytest

from app.decision import DrivingAction, MockDrivingAgent


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("steering", -1.01),
        ("steering", 1.01),
        ("throttle", -0.01),
        ("throttle", 1.01),
        ("brake", -0.01),
        ("brake", 1.01),
    ],
)
def test_action_rejects_out_of_range_values(field: str, value: float) -> None:
    values = {"steering": 0.0, "throttle": 0.0, "brake": 0.0}
    values[field] = value

    with pytest.raises(ValueError):
        DrivingAction(**values)


@pytest.mark.parametrize(
    "action",
    [
        DrivingAction(-1.0, 0.0, 0.0),
        DrivingAction(1.0, 1.0, 1.0),
        DrivingAction(0.0, 0.5, 0.5),
    ],
)
def test_action_accepts_normalized_values(action: DrivingAction) -> None:
    assert -1.0 <= action.steering <= 1.0
    assert 0.0 <= action.throttle <= 1.0
    assert 0.0 <= action.brake <= 1.0


def test_mock_driving_agent_returns_safe_action() -> None:
    action = MockDrivingAgent().predict(np.zeros((32, 32, 3), dtype=np.uint8))

    assert action == DrivingAction(0.0, 0.0, 0.0)
