# Overview

swarm-coordinator provides simple Python primitives for coordinating multiple simulated UAV agents.

The package focuses on the layer between individual vehicle movement and higher-level swarm planning. It gives developers reusable pieces for experiments, tutorials, research prototypes, and early-stage planning tools.

## What It Includes

- Agent state
- Position and waypoint primitives
- Formation target generation
- Simple task assignment
- Minimum separation checks
- Fixed-step simulation

## What It Does Not Include

- Real UAV control
- Hardware integration
- Autopilot communication
- Certified collision avoidance
- Airspace compliance checks
- Real-time guarantees
- Sensor fusion

## Design Principles

The package is intentionally small and dependency-light. Each primitive should be easy to inspect, test, and adapt.
