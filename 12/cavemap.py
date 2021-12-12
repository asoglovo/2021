import fileinput
from typing import Callable, List, Set


Node = str
Path = List[str]
ValidateNodeFn = Callable[[Node, Path], bool]

start = 'start'
end = 'end'


class MapBiEdge:
    """
    Bidirectional edge: 'a-b == b-a' and 'hash(a-b) == hash(b-a)'.
    """

    def __init__(self, node_a: Node, node_b: Node):
        self.node_a = node_a
        self.node_b = node_b

    def __eq__(self, other) -> bool:
        if self is None:
            return False

        if self is other:
            return True

        return set([self.node_a, self.node_b]) == set([other.node_a, other.node_b])

    def __hash__(self) -> int:
        return hash(self.node_a) ^ hash(self.node_b)

    def __repr__(self) -> str:
        return f'{self.node_a}-{self.node_b}'

    def has_node(self, node: str) -> bool:
        return node == self.node_a or node == self.node_b

    def opposite_node(self, node: Node) -> Node:
        if not self.has_node(node):
            raise ValueError(f'Node {node} not found in edge {self}.')

        return self.node_a if node == self.node_b else self.node_b


def read_cave_map():
    edges = set()

    for line in fileinput.input():
        node_a, node_b = line.strip().split('-')
        edges.add(MapBiEdge(node_a, node_b))

    return edges


def find_all_paths(
    edges: Set[MapBiEdge],
    validate_next_node: ValidateNodeFn,
) -> List[Path]:
    """
    Finds all possible paths going from 'start' to 'end' and don't visit small caves
    more than once. Big caves can be visited multiple times.
    """

    def extend_path(path: Path) -> List[Path]:
        paths = []

        for node in next_path_nodes(path):
            if node == end:
                paths.append(path + [node])
            else:
                paths.extend(
                    extend_path(path + [node])
                )

        return paths

    def next_path_nodes(path: Path) -> List[Node]:
        last_node = path[-1]
        visitable_nodes = visitable_nodes_from(last_node)

        return [
            node for node in visitable_nodes
            if validate_next_node(node, path)
        ]

    def visitable_nodes_from(start: Node) -> List[Node]:
        return [
            edge.opposite_node(start)
            for edge in edges if edge.has_node(start)
        ]

    return extend_path([start])
