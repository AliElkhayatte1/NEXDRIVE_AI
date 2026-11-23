"""Interfaces and safe mock implementations for driving decisions."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class DrivingAction:
    """Normalized vehicle command produced by a driving agent."""

    steering: float
    throttle: float
    brake: float

    def __post_init__(self) -> None:
        if not -1.0 <= self.steering <= 1.0:
            raise ValueError("steering must be between -1 and 1")
        if not 0.0 <= self.throttle <= 1.0:
            raise ValueError("throttle must be between 0 and 1")
        if not 0.0 <= self.brake <= 1.0:
            raise ValueError("brake must be between 0 and 1")


class DrivingAgent(ABC):
    """Interface for models that map an image to a driving action."""

    @abstractmethod
    def predict(self, image: np.ndarray) -> DrivingAction:
        """Return a normalized action for the supplied image."""
        raise NotImplementedError


class MockDrivingAgent(DrivingAgent):
    """Deterministic test agent that always recommends a safe neutral stop."""

    def predict(self, image: np.ndarray) -> DrivingAction:
        if not isinstance(image, np.ndarray):
            raise TypeError("image must be a NumPy array")
        if image.size == 0:
            raise ValueError("image must not be empty")
        return DrivingAction(steering=0.0, throttle=0.0, brake=0.0)
