from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from .agent import UAVAgent
from .collision import SeparationAlert, separation_alerts
from .formation import assign_formation_waypoints, grid_formation, line_formation, v_formation
from .types import Position, Waypoint


@dataclass
class SwarmCoordinator:
    """Coordinate a collection of UAV agents in simulation-oriented workflows."""

    agents: list[UAVAgent]
    minimum_separation_m: float = 5.0

    def __post_init__(self) -> None:
        if self.minimum_separation_m <= 0:
            raise ValueError("minimum_separation_m must be positive")
        ids = [agent.agent_id for agent in self.agents]
        if len(ids) != len(set(ids)):
            raise ValueError("agent IDs must be unique")

    def get_agent(self, agent_id: str) -> UAVAgent:
        for agent in self.agents:
            if agent.agent_id == agent_id:
                return agent
        raise KeyError(f"unknown agent_id: {agent_id}")

    def set_agent_waypoints(self, agent_id: str, waypoints: Sequence[Waypoint]) -> None:
        self.get_agent(agent_id).set_waypoints(waypoints)

    def set_line_formation(self, anchor: Position, spacing_m: float, axis: str = "x") -> dict[str, Waypoint]:
        positions = line_formation(anchor, len(self.agents), spacing_m, axis=axis)
        return assign_formation_waypoints(self.agents, positions)

    def set_grid_formation(self, anchor: Position, spacing_m: float, columns: int | None = None) -> dict[str, Waypoint]:
        positions = grid_formation(anchor, len(self.agents), spacing_m, columns=columns)
        return assign_formation_waypoints(self.agents, positions)

    def set_v_formation(self, anchor: Position, spacing_m: float) -> dict[str, Waypoint]:
        positions = v_formation(anchor, len(self.agents), spacing_m)
        return assign_formation_waypoints(self.agents, positions)

    def step(self, dt_seconds: float) -> list[SeparationAlert]:
        for agent in self.agents:
            agent.step(dt_seconds)
        return self.separation_alerts()

    def separation_alerts(self) -> list[SeparationAlert]:
        return separation_alerts(self.agents, self.minimum_separation_m)

    def all_idle(self) -> bool:
        return all(agent.target is None for agent in self.agents)
