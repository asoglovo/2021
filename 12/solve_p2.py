from collections import Counter

from cavemap import Node, Path, find_all_paths, read_cave_map


def validate_next_node(node: Node, path: Path) -> bool:
    """
    Checks whether the given next node can be added to the path.

    The rules are:
    - If the node is a big cave, it can always be added to the path.
    - If the node is a small cave:
        - it can be added if the cave is not yet in the path
        - it can be added if the cave is already once in the path and no
          other small cave appears twice in the path.
    """
    if node.isupper():
        return True

    if node == 'start':
        return False

    small_caves_counter = Counter([node for node in path if node.islower()])
    if node not in small_caves_counter:
        return True

    return small_caves_counter.most_common(1)[0][1] == 1


if __name__ == '__main__':
    edges = read_cave_map()
    paths = find_all_paths(edges, validate_next_node)

    print(f'There are {len(paths)} distinct paths.')
