from cavemap import find_all_paths, read_cave_map, Node, Path


def validate_next_node(node: Node, path: Path) -> bool:
    """
    Checks whether the given next node can be added to the path.

    The rules are:
        - If the node is a big cave, it can always be added to the path.
        - If the node is a small cave it can be added if the cave is not 
          yet in the path.
    """
    if node.isupper():
        return True

    small_caves_in_path = set([node for node in path if node.islower()])
    return node not in small_caves_in_path


if __name__ == '__main__':
    edges = read_cave_map()
    paths = find_all_paths(edges, validate_next_node)

    print(f'There are {len(paths)} distinct paths.')
