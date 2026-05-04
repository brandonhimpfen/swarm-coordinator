from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from .agent import UAVAgent


@dataclass(frozen=True)
class SeparationAlert:
    """A pairwise minimum-separation warning."""

    agent_a: str
    agent_b: str
    distance_m: float
    minimum_distance_m: float


def pairwise_distances(agents: Sequence[UAVAgent]) -> dict[tuple[str, str], float]:
    """Return all pairwise distances between agents."""
    distances: dict[tuple[str, str], float] = {}
    for i, agent_a in enumerate(agents):
        for agent_b in agents[i + 1 :]:
            distances[(agent_a.agent_id, agent_b.agent_id)] = agent_a.distance_to(agent_b)
    return distances


def separation_alerts(agents: Sequence[UAVAgent], minimum_distance_m: float) -> list[SeparationAlert]:
    """Return alerts for any agent pair closer than the minimum separation."""
    if minimum_distance_m <= 0:
        raise ValueError("minimum_distance_m must be positive")

    alerts: list[SeparationAlert] = []
    for (agent_a, agent_b), distance in pairwise_distances(agents).items():
        if distance < minimum_distance_m:
            alerts.append(SeparationAlert(agent_a, agent_b, distance, minimum_distance_m))
    return alerts
