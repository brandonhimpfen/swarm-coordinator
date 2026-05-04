from __future__ import annotations

from dataclasses import dataclass, field

from .collision import SeparationAlert
from .coordinator import SwarmCoordinator


@dataclass(frozen=True)
class SimulationFrame:
    """A snapshot of a swarm simulation step."""

    time_seconds: float
    positions: dict[str, tuple[float, float, float]]
    alerts: list[SeparationAlert] = field(default_factory=list)


def run_simulation(
    coordinator: SwarmCoordinator,
    dt_seconds: float = 1.0,
    max_steps: int = 120,
    stop_when_idle: bool = True,
) -> list[SimulationFrame]:
    """Run a simple fixed-time-step simulation."""
    if dt_seconds <= 0:
        raise ValueError("dt_seconds must be positive")
    if max_steps <= 0:
        raise ValueError("max_steps must be positive")

    frames: list[SimulationFrame] = []
    elapsed = 0.0
    for _ in range(max_steps):
        alerts = coordinator.step(dt_seconds)
        elapsed += dt_seconds
        frames.append(
            SimulationFrame(
                time_seconds=elapsed,
                positions={
                    agent.agent_id: (agent.position.x, agent.position.y, agent.position.z)
                    for agent in coordinator.agents
                },
                alerts=alerts,
            )
        )
        if stop_when_idle and coordinator.all_idle():
            break
    return frames
