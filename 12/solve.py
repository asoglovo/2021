from cavemap import find_all_paths, read_cave_map

if __name__ == '__main__':
    nodes, edges = read_cave_map()
    paths = find_all_paths(edges)

    for path in paths:
        print('-'.join(path))

    print(f'There are {len(paths)} distinct paths.')
