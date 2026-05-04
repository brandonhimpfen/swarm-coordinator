from __future__ import annotations

from collections.abc import Sequence

from .agent import UAVAgent
from .types import Position, Waypoint


def line_formation(anchor: Position, count: int, spacing_m: float, axis: str = "x") -> list[Position]:
    """Return positions arranged in a centered line formation."""
    _validate_count_spacing(count, spacing_m)
    if axis not in {"x", "y"}:
        raise ValueError("axis must be 'x' or 'y'")

    offset = (count - 1) / 2
    positions: list[Position] = []
    for i in range(count):
        delta = (i - offset) * spacing_m
        positions.append(anchor.translate(dx=delta if axis == "x" else 0, dy=delta if axis == "y" else 0))
    return positions


def grid_formation(anchor: Position, count: int, spacing_m: float, columns: int | None = None) -> list[Position]:
    """Return positions arranged in a compact grid formation."""
    _validate_count_spacing(count, spacing_m)
    if columns is None:
        columns = max(1, int(count**0.5))
    if columns <= 0:
        raise ValueError("columns must be positive")

    positions: list[Position] = []
    for i in range(count):
        row = i // columns
        col = i % columns
        positions.append(anchor.translate(dx=col * spacing_m, dy=row * spacing_m))
    return positions


def v_formation(anchor: Position, count: int, spacing_m: float) -> list[Position]:
    """Return positions arranged in a leader-centered V formation."""
    _validate_count_spacing(count, spacing_m)
    positions = [anchor]
    layer = 1
    while len(positions) < count:
        positions.append(anchor.translate(dx=-layer * spacing_m, dy=layer * spacing_m))
        if len(positions) >= count:
            break
        positions.append(anchor.translate(dx=layer * spacing_m, dy=layer * spacing_m))
        layer += 1
    return positions


def assign_formation_waypoints(
    agents: Sequence[UAVAgent],
    positions: Sequence[Position],
    hold_seconds: float = 0.0,
) -> dict[str, Waypoint]:
    """Assign one formation waypoint to each agent in sequence."""
    if len(agents) != len(positions):
        raise ValueError("agents and positions must have the same length")
    assignments = {agent.agent_id: Waypoint(position, hold_seconds) for agent, position in zip(agents, positions)}
    for agent in agents:
        agent.set_waypoints([assignments[agent.agent_id]])
    return assignments


def _validate_count_spacing(count: int, spacing_m: float) -> None:
    if count <= 0:
        raise ValueError("count must be positive")
    if spacing_m <= 0:
        raise ValueError("spacing_m must be positive")
