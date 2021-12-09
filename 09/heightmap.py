
from typing import Dict, List, Set, Tuple


HeightMap = List[List[int]]
Basin = Set[Tuple[int, int]]

height_outside_map = 1000000


def find_low_points(heightmap: HeightMap):
    """
    Finds the low points in a heightmap: the locations that are lower than any 
    of its adjacent locations. Most locations have four adjacent locations (up, 
    down, left, and right); locations on the edge or corner of the map have 
    three or two adjacent locations, respectively. (Diagonal locations do not 
    count as adjacent.)

    The risk level of a low point is 1 plus its height.
    """
    low_points = []

    for i, row in enumerate(heightmap):
        for j, num in enumerate(row):
            if is_low_point(heightmap, i, j):
                low_points.append(
                    {'pos': (i, j), 'height': num, 'risk': num + 1}
                )

    return low_points


def is_low_point(heightmap: HeightMap, row: int, col: int) -> bool:
    """
    Checks whether a given location is lower than any of its adjacent locations.
    """
    height = heightmap[row][col]

    left_height = __get_height(heightmap, row, col - 1)
    if height >= left_height:
        return False

    right_height = __get_height(heightmap, row, col + 1)
    if height >= right_height:
        return False

    up_height = __get_height(heightmap, row - 1, col)
    if height >= up_height:
        return False

    down_height = __get_height(heightmap, row + 1, col)
    if height >= down_height:
        return False

    return True


def __get_height(heightmap: HeightMap, row: int, col: int) -> int:
    """
    Returns the height of the heightmap at the given location.
    If the index is out ouf bounds, returns a large number.
    """
    if not 0 <= row < len(heightmap):
        return height_outside_map

    if not 0 <= col < len(heightmap[row]):
        return height_outside_map

    return heightmap[row][col]


def find_basin_size(heightmap: HeightMap, low_point: Dict):
    """
    A basin is all locations that eventually flow downward to a single low point. 
    Therefore, every low point has a basin, although some basins are very small. 
    Locations of height 9 do not count as being in any basin, and all other locations 
    will always be part of exactly one basin.

    The size of a basin is the number of locations within the basin, including the 
    low point.
    """
    i, j = low_point['pos']
    basin_positions = __find_basin_recursive(heightmap, i, j)

    return len(basin_positions) + 1


def __find_basin_recursive(heightmap: HeightMap, row: int, col: int) -> Basin:
    """
    Returns a list of neighbour positions from the given location that are valid 
    for flowing to the given position. It keeps looking for neighbours until it
    finds one with a height of 9 or a border.
    """
    basin_positions = __find_basin(heightmap, row, col)

    neighbour_basin_pos = set()
    for i, j in basin_positions:
        positions = __find_basin_recursive(heightmap, i, j)
        neighbour_basin_pos.update(
            [pos for pos in positions if pos not in basin_positions]
        )

    basin_positions.update(neighbour_basin_pos)

    return basin_positions


def __find_basin(heightmap: HeightMap, row: int, col: int) -> Basin:
    """
    Returns a list of neighbour positions from the given location that are valid 
    for flowing to the given position.
    """
    heigh = heightmap[row][col]
    positions = set()

    left_height = __get_height(heightmap, row, col - 1)
    if heigh < left_height and left_height < 9:
        positions.add((row, col - 1))

    right_height = __get_height(heightmap, row, col + 1)
    if heigh < right_height and right_height < 9:
        positions.add((row, col + 1))

    up_height = __get_height(heightmap, row - 1, col)
    if heigh < up_height and up_height < 9:
        positions.add((row - 1, col))

    down_height = __get_height(heightmap, row + 1, col)
    if heigh < down_height and down_height < 9:
        positions.add((row + 1, col))

    return positions
