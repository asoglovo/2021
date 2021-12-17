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

    def risk_at(position: Tuple[int, int]) -> int:
        i, j = position
        return risk_map[i][j]

    def nodes_reachable_from(pos: Tuple[int, int]) -> Path:
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

    def trace_safest_path_back(risks, path: Path) -> Path:
        while path[-1] != start:
            best_node, _ = min(
                [
                    (node, risks[node])
                    for node in nodes_reachable_from(path[-1])
                ],
                key=lambda x: x[1]
            )
            path.append(best_node)

        return path

    nodes = list([(i, j) for i in range(size) for j in range(size)])
    risks = defaultdict(lambda: infinity)
    risks[start] = 0

    for node in nodes[1:]:
        for neighbor in nodes_reachable_from(node):
            risks[node] = min(risks[node], risks[neighbor] + risk_at(node))

    # for i in range(size):
    #     for j in range(size):
    #         print(f'{risks[(i, j)]:3}', end=' ')
    #     print()

    path = trace_safest_path_back(risks, [end])
    path.reverse()

    return path, risks[end]


def risk_for_path(risk_map: RiskMap, path: Path) -> int:
    return sum(
        risk_map[node[0]][node[1]] for node in path if node != (0, 0)
    )


def print_path(risk_map: RiskMap, path: Path):
    path_set = set(path)

    for i, row in enumerate(risk_map):
        for j, cell in enumerate(row):
            if (i, j) in path_set:
                print(f'[{cell}]', end='')
            else:
                print(f' {cell} ', end='')
        print()
