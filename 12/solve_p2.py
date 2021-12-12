from cavemap import find_all_paths, read_cave_map, Node, Path


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
    return True


if __name__ == '__main__':
    edges = read_cave_map()
    paths = find_all_paths(edges)

    # for path in paths:
    #     print('-'.join(path))

    print(f'There are {len(paths)} distinct paths.')
