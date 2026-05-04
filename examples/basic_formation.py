from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from swarm_coordinator import Position, SwarmCoordinator, UAVAgent, run_simulation


def main() -> None:
    agents = [
        UAVAgent("uav-1", Position(0, 0, 20), max_speed_mps=8),
        UAVAgent("uav-2", Position(0, 10, 20), max_speed_mps=8),
        UAVAgent("uav-3", Position(0, 20, 20), max_speed_mps=8),
        UAVAgent("uav-4", Position(0, 30, 20), max_speed_mps=8),
        UAVAgent("uav-5", Position(0, 40, 20), max_speed_mps=8),
    ]

    coordinator = SwarmCoordinator(agents, minimum_separation_m=6)
    coordinator.set_v_formation(anchor=Position(100, 100, 20), spacing_m=15)

    frames = run_simulation(coordinator, dt_seconds=1, max_steps=30)
    final_frame = frames[-1]

    print(f"Simulated {len(frames)} frames")
    for agent_id, position in final_frame.positions.items():
        print(agent_id, position)
    print(f"Final alerts: {len(final_frame.alerts)}")


if __name__ == "__main__":
    main()
