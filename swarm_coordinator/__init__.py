"""Multi-UAV coordination primitives for simulation and research workflows."""

from .agent import UAVAgent
from .assignment import nearest_target_assignment
from .collision import SeparationAlert, pairwise_distances, separation_alerts
from .coordinator import SwarmCoordinator
from .formation import assign_formation_waypoints, grid_formation, line_formation, v_formation
from .simulation import SimulationFrame, run_simulation
from .types import Position, Waypoint

__all__ = [
    "Position",
    "Waypoint",
    "UAVAgent",
    "SwarmCoordinator",
    "SeparationAlert",
    "SimulationFrame",
    "line_formation",
    "grid_formation",
    "v_formation",
    "assign_formation_waypoints",
    "pairwise_distances",
    "separation_alerts",
    "nearest_target_assignment",
    "run_simulation",
]

__version__ = "0.1.0"
