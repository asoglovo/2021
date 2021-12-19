from collections import defaultdict
from typing import List, Tuple

Position = Tuple[int, int]
Path = List[Position]

infinity = float('inf')


def find_safest_path(risk_map) -> Tuple[Path, int]:
    """
    Returns the safest path through the risk map along with its risk score.
    """
    return dijkstra(risk_map)


def print_risks(size: int, risks, path):
    for i in range(size):
        for j in range(size):
            if (i, j) in path:
                print(f'[{risks[(i, j)]:3}]', end='')
            else:
                print(f' {risks[(i, j)]:3} ', end='')
        print()


def dijkstra(risk_map) -> Tuple[Path, int]:
    """
    Finds the shortest path from the top-left corner to the bottom-right using
    DiJkstra's algorithm.
    """
    size = risk_map.size
    start = (0, 0)
    end = (size - 1, size - 1)

    unvisited_nodes = set(
        [(i, j) for i in range(size) for j in range(size)]
    )
    distances = defaultdict(lambda: infinity)
    prev_nodes = defaultdict(lambda: None)

    distances[start] = 0

    while end in unvisited_nodes:
        min_node, min_distance = min(
            [(node, distances[node]) for node in unvisited_nodes],
            key=lambda x: x[1]
        )

        unvisited_nodes.remove(min_node)

        neighbors = [
            node for node in risk_map.nodes_reachable_from(min_node)
            if node in unvisited_nodes
        ]
        for neighbor in neighbors:
            new_distance = min_distance + risk_map[neighbor]
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                prev_nodes[neighbor] = min_node

    path = [end]
    while path[0] != start:
        path.insert(0, prev_nodes[path[0]])

    return path, distances[end]


# nums = [i for i in range(1, 10)]


# def risk_at_extended(risk_map: RiskMap, position: Position) -> int:
#     size = len(risk_map)
#     i, j = position
#     times_bottom = i // size
#     times_right = j // size

#     value = risk_map[i % size][j % size]
#     idx = nums.index(value)
#     new_idx = (idx + times_bottom + times_right) % len(nums)

#     return nums[new_idx]
