from __future__ import annotations

from collections.abc import Sequence

from .agent import UAVAgent
from .types import Position


def nearest_target_assignment(
    agents: Sequence[UAVAgent], targets: Sequence[Position]
) -> dict[str, Position]:
    """Greedily assign each agent to its nearest remaining target."""
    if len(agents) > len(targets):
        raise ValueError("number of targets must be at least number of agents")

    remaining = list(targets)
    assignments: dict[str, Position] = {}
    for agent in agents:
        nearest = min(remaining, key=lambda target: agent.position.distance_to(target))
        assignments[agent.agent_id] = nearest
        remaining.remove(nearest)
    return assignments
