import fileinput
from typing import List, Tuple
from collections import defaultdict

RiskMap = List[List[int]]
Path = List[Tuple[int, int]]

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
    size = len(risk_map)
    start = (0, 0)
    end = (size - 1, size - 1)

    def risk_at(position):
        i, j = position
        return risk_map[i][j]

    def nodes_reachable_from(pos: Tuple[int, int]) -> List[Tuple[int, int]]:
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

    # visited = set()
    path = []
    nodes = list([(i, j) for i in range(size) for j in range(size)])
    risks = defaultdict(lambda: infinity)
    risks[start] = 0  # risk_at(start)
    # risks = dict(
    #     [(node, risk_at(start)) if node == start else (node, infinity)
    #      for node in nodes]
    # )

    for node in nodes:
        for neighbor in nodes_reachable_from(node):
            risks[node] = min(risks[node], risks[neighbor] + risk_at(node))

    for i in range(size):
        for j in range(size):
            print(f'{risks[(i, j)]:2}', end=' ')
        print()

    return path, risks[end]


def print_path(risk_map: RiskMap, path: Path):
    path_set = set(path)

    for i, row in enumerate(risk_map):
        for j, cell in enumerate(row):
            if (i, j) in path_set:
                print(f'[{cell}]', end='')
            else:
                print(f' {cell} ', end='')
        print()
