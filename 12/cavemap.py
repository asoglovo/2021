import fileinput
from typing import List, Set


Node = str
Path = List[str]

start_node = 'start'
end_node = 'end'


class MapBiEdge:
    """
    Bidirectional edge: a-b == b-a and hash(a-b) == hash(b-a).
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
    nodes = set()

    for line in fileinput.input():
        node_a, node_b = line.strip().split('-')
        edges.add(MapBiEdge(node_a, node_b))
        nodes.add(node_a)
        nodes.add(node_b)

    return nodes, edges


def find_all_paths(
    edges: Set[MapBiEdge],
    start: Node = start_node,
    end: Node = end_node
) -> List[Path]:
    """
    Finds all possible paths going from 'start' to 'end' and don't visit small caves
    more than once. Big caves can be visited multiple times.
    """
    return __extend_path([start], edges, end)


def __extend_path(path: Path, edges: Set[MapBiEdge], end: Node) -> List[Path]:
    paths = []

    for node in __next_path_nodes(path, edges):
        if node == end:
            paths.append(path + [node])
        else:
            paths.extend(__extend_path(path + [node], edges, end))

    return paths


def __next_path_nodes(path: Path, edges: Set[MapBiEdge]) -> List[Node]:
    """
    Given a path of nodes, finds the next visitable nodes. Small caves can't 
    appear more than once in the path.
    """
    last_node = path[-1]
    small_caves_in_path = set([node for node in path if __is_small_cave(node)])
    visitable_nodes = __visitable_nodes_from(last_node, edges)

    return [
        node for node in visitable_nodes
        if node not in small_caves_in_path
    ]


def __visitable_nodes_from(start: Node, edges: Set[MapBiEdge]) -> List[Node]:
    """
    Finds all nodes that can be reached from 'start' node.
    """
    return [
        edge.opposite_node(start)
        for edge in edges if edge.has_node(start)
    ]


def __is_small_cave(node: Node) -> bool:
    """
    Checks if the node is a small cave.
    Small caves are those whose name is in all lowercase letters.
    """
    return node.islower()
