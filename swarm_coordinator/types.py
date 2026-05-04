from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Position:
    """A simple 3D position in meters."""

    x: float
    y: float
    z: float = 0.0

    def distance_to(self, other: "Position") -> float:
        """Return Euclidean distance to another position."""
        return math.sqrt(
            (self.x - other.x) ** 2
            + (self.y - other.y) ** 2
            + (self.z - other.z) ** 2
        )

    def translate(self, dx: float = 0.0, dy: float = 0.0, dz: float = 0.0) -> "Position":
        """Return a new position translated by the supplied offsets."""
        return Position(self.x + dx, self.y + dy, self.z + dz)

    def move_towards(self, target: "Position", max_distance: float) -> "Position":
        """Move toward target by at most max_distance."""
        if max_distance < 0:
            raise ValueError("max_distance must be non-negative")

        distance = self.distance_to(target)
        if distance == 0 or distance <= max_distance:
            return target

        ratio = max_distance / distance
        return Position(
            self.x + (target.x - self.x) * ratio,
            self.y + (target.y - self.y) * ratio,
            self.z + (target.z - self.z) * ratio,
        )


@dataclass(frozen=True)
class Waypoint:
    """A waypoint with an optional hold time in seconds."""

    position: Position
    hold_seconds: float = 0.0

    def __post_init__(self) -> None:
        if self.hold_seconds < 0:
            raise ValueError("hold_seconds must be non-negative")
