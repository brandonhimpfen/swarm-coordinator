from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

from .types import Position, Waypoint


@dataclass
class UAVAgent:
    """A lightweight UAV agent for swarm simulation and coordination experiments."""

    agent_id: str
    position: Position
    max_speed_mps: float = 5.0
    metadata: dict[str, str] = field(default_factory=dict)
    waypoints: list[Waypoint] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.agent_id:
            raise ValueError("agent_id is required")
        if self.max_speed_mps <= 0:
            raise ValueError("max_speed_mps must be positive")

    def set_waypoints(self, waypoints: Iterable[Waypoint]) -> None:
        self.waypoints = list(waypoints)

    @property
    def target(self) -> Waypoint | None:
        return self.waypoints[0] if self.waypoints else None

    def step(self, dt_seconds: float) -> None:
        """Advance the agent toward its current waypoint."""
        if dt_seconds <= 0:
            raise ValueError("dt_seconds must be positive")
        target = self.target
        if target is None:
            return

        max_distance = self.max_speed_mps * dt_seconds
        self.position = self.position.move_towards(target.position, max_distance)

        if self.position == target.position:
            self.waypoints.pop(0)

    def distance_to(self, other: "UAVAgent") -> float:
        return self.position.distance_to(other.position)
