from swarm_coordinator import Position, SwarmCoordinator, UAVAgent, run_simulation


def test_run_simulation_stops_when_idle() -> None:
    coordinator = SwarmCoordinator([UAVAgent("a", Position(0, 0), max_speed_mps=10)])
    coordinator.set_line_formation(Position(10, 0), spacing_m=5)
    frames = run_simulation(coordinator, dt_seconds=1, max_steps=10)
    assert len(frames) == 1
    assert frames[-1].positions["a"] == (10, 0, 0)
