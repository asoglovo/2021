import fileinput
from typing import Dict, List, Tuple
from collections import defaultdict

RiskMap = List[List[int]]
Position = Tuple[int, int]
Path = List[Position]

infinity = float('inf')


def read_risk_map() -> RiskMap:
    return [
        [int(n) for n in line.strip()]
        for line in fileinput.input()
    ]


def find_safest_path(risk_map: RiskMap) -> Tuple[Path, int]:
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


def print_path(risk_map: RiskMap, path: Path):
    path_set = set(path)

    for i, row in enumerate(risk_map):
        for j, cell in enumerate(row):
            if (i, j) in path_set:
                print(f'[{cell}]', end='')
            else:
                print(f' {cell} ', end='')
        print()


def dijkstra(risk_map: RiskMap) -> Tuple[Path, int]:
    """
    Finds the shortest path from the top-left corner to the bottom-right using
    DiJkstra's algorithm.
    """
    size = len(risk_map)
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
            node for node in nodes_reachable_from(risk_map, min_node)
            if node in unvisited_nodes
        ]
        for neighbor in neighbors:
            new_distance = min_distance + risk_at(risk_map, neighbor)
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                prev_nodes[neighbor] = min_node

    path = [end]
    while path[0] != start:
        path.insert(0, prev_nodes[path[0]])

    return path, distances[end]


def nodes_reachable_from(risk_map: RiskMap, pos: Position) -> Path:
    size = len(risk_map)
    i, j = pos

    return filter(
        lambda ij: 0 <= ij[0] < size and 0 <= ij[1] < size,
        [
            (i - 1, j),
            (i, j + 1),
            (i + 1, j),
            (i, j - 1)
        ]
    )


def risk_at(risk_map: RiskMap, position: Position) -> int:
    i, j = position
    return risk_map[i][j]
