from swarm_coordinator import Position, UAVAgent, nearest_target_assignment


def test_nearest_target_assignment() -> None:
    agents = [UAVAgent("a", Position(0, 0)), UAVAgent("b", Position(100, 0))]
    targets = [Position(90, 0), Position(10, 0)]
    assignments = nearest_target_assignment(agents, targets)
    assert assignments["a"] == Position(10, 0, 0)
    assert assignments["b"] == Position(90, 0, 0)
