# swarm-coordinator

**swarm-coordinator** is a lightweight Python toolkit for experimenting with multi-UAV coordination primitives, including agent movement, formations, task assignment, spacing checks, and simple simulation workflows.

It is designed for education, research prototypes, planning tools, and simulation-oriented workflows. It is **not** a flight controller and should not be used to command real UAVs without a validated safety, autonomy, communications, and regulatory stack.

## Features

- UAV agent model with position, speed, metadata, and waypoint queues
- 3D position and waypoint primitives
- Line, grid, and V formation helpers
- Formation waypoint assignment
- Pairwise distance calculations
- Minimum-separation alert checks
- Greedy nearest-target assignment
- Fixed-step swarm simulation loop
- Examples and tests

## Installation

```bash
pip install -e .
```

For development:

```bash
pip install -e ".[dev]"
```

## Quick Start

```python
from swarm_coordinator import Position, SwarmCoordinator, UAVAgent, run_simulation

agents = [
    UAVAgent("uav-1", Position(0, 0, 20), max_speed_mps=8),
    UAVAgent("uav-2", Position(0, 10, 20), max_speed_mps=8),
    UAVAgent("uav-3", Position(0, 20, 20), max_speed_mps=8),
]

coordinator = SwarmCoordinator(agents, minimum_separation_m=6)
coordinator.set_v_formation(anchor=Position(100, 100, 20), spacing_m=15)

frames = run_simulation(coordinator, dt_seconds=1, max_steps=30)
print(frames[-1].positions)
```

## Core Concepts

- **Agent**: A `UAVAgent` represents a simulated UAV with an ID, position, maximum speed, and optional waypoint queue.
- **Formation**: Formation helpers generate target positions for a swarm. The initial release includes line, grid, and V formations.
- **Coordinator**: `SwarmCoordinator` manages a list of agents, assigns formations, advances the swarm through time, and checks spacing alerts.
- **Separation Alerts**: The package can detect when two simulated UAV agents are closer than a configured minimum separation distance.
- **Simulation**: The simulation loop is intentionally simple. It advances each agent toward its current waypoint using fixed time steps and records position frames.

## Examples

Run the basic formation example:

```bash
python examples/basic_formation.py
```

Run the task assignment example:

```bash
python examples/task_assignment.py
```

## Testing

```bash
pytest
```

## Safety Notice

This package is for simulation, learning, and research prototypes. It does not include airworthiness checks, real-time guarantees, communication protocols, obstacle avoidance, regulatory compliance tooling, fail-safe behaviour, or hardware integration.

Do not use this package to directly control real UAVs.

## Roadmap

Potential future improvements:

- More formation patterns
- Formation transitions
- Collision-risk prediction
- Geospatial coordinate support
- Mission import/export formats
- Visualization utilities
- ROS/MAVLink-adjacent adapters for simulation use only
- More advanced assignment algorithms

## License

MIT License.
