from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from swarm_coordinator import Position, UAVAgent, nearest_target_assignment

agents = [
    UAVAgent("survey-1", Position(0, 0, 10)),
    UAVAgent("survey-2", Position(50, 0, 10)),
    UAVAgent("survey-3", Position(100, 0, 10)),
]

targets = [
    Position(10, 20, 10),
    Position(60, 25, 10),
    Position(120, 15, 10),
]

assignments = nearest_target_assignment(agents, targets)

for agent_id, target in assignments.items():
    print(f"{agent_id} -> {target}")
