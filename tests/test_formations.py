from swarm_coordinator import Position, grid_formation, line_formation, v_formation


def test_line_formation_is_centered() -> None:
    positions = line_formation(Position(0, 0, 10), count=3, spacing_m=5)
    assert positions == [Position(-5, 0, 10), Position(0, 0, 10), Position(5, 0, 10)]


def test_grid_formation_count() -> None:
    positions = grid_formation(Position(0, 0), count=5, spacing_m=10, columns=2)
    assert len(positions) == 5
    assert positions[-1] == Position(0, 20, 0)


def test_v_formation_count() -> None:
    positions = v_formation(Position(0, 0), count=5, spacing_m=10)
    assert len(positions) == 5
    assert positions[0] == Position(0, 0, 0)
