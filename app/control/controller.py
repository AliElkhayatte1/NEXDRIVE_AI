"""Safe vehicle-controller interfaces; real input control is excluded."""

from abc import ABC, abstractmethod

from app.decision.agent import DrivingAction


class VehicleController(ABC):
    """Interface for applying and stopping vehicle actions."""

    @abstractmethod
    def apply_action(self, action: DrivingAction) -> None:
        """Apply a normalized driving action."""
        raise NotImplementedError

    @abstractmethod
    def emergency_stop(self) -> None:
        """Immediately stop or disable future vehicle control."""
        raise NotImplementedError


class MockVehicleController(VehicleController):
    """Safe controller that only records commands in memory."""

    def __init__(self) -> None:
        self.last_action: DrivingAction | None = None
        self.commands: list[DrivingAction] = []
        self.stopped = False

    def apply_action(self, action: DrivingAction) -> None:
        if self.stopped:
            return
        self.last_action = action
        self.commands.append(action)

    def emergency_stop(self) -> None:
        self.stopped = True
        self.last_action = None
