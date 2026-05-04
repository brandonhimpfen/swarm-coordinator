from swarm_coordinator import Position, UAVAgent, Waypoint


def test_agent_moves_towards_waypoint() -> None:
    agent = UAVAgent("a", Position(0, 0), max_speed_mps=5)
    agent.set_waypoints([Waypoint(Position(10, 0))])
    agent.step(1)
    assert agent.position == Position(5, 0, 0)


def test_agent_reaches_waypoint_and_clears_target() -> None:
    agent = UAVAgent("a", Position(0, 0), max_speed_mps=20)
    agent.set_waypoints([Waypoint(Position(10, 0))])
    agent.step(1)
    assert agent.position == Position(10, 0, 0)
    assert agent.target is None
