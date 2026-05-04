from swarm_coordinator import Position, UAVAgent, separation_alerts


def test_separation_alerts_detect_close_agents() -> None:
    agents = [UAVAgent("a", Position(0, 0)), UAVAgent("b", Position(3, 4))]
    alerts = separation_alerts(agents, minimum_distance_m=6)
    assert len(alerts) == 1
    assert alerts[0].distance_m == 5


def test_separation_alerts_ignore_safe_agents() -> None:
    agents = [UAVAgent("a", Position(0, 0)), UAVAgent("b", Position(10, 0))]
    assert separation_alerts(agents, minimum_distance_m=6) == []
