from app.control import MockVehicleController
from app.decision import DrivingAction


def test_mock_controller_records_action_without_external_control() -> None:
    controller = MockVehicleController()
    action = DrivingAction(0.25, 0.5, 0.0)

    controller.apply_action(action)

    assert controller.last_action == action
    assert controller.commands == [action]


def test_mock_controller_emergency_stop_prevents_new_commands() -> None:
    controller = MockVehicleController()
    controller.apply_action(DrivingAction(0.0, 0.5, 0.0))

    controller.emergency_stop()
    controller.apply_action(DrivingAction(0.0, 1.0, 0.0))

    assert controller.stopped is True
    assert controller.last_action is None
    assert len(controller.commands) == 1
