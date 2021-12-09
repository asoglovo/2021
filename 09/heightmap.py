
from typing import List


HeightMap = List[List[int]]


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

    left_height = __get_heightmap_height(heightmap, row, col - 1)
    if height >= left_height:
        return False

    right_height = __get_heightmap_height(heightmap, row, col + 1)
    if height >= right_height:
        return False

    up_height = __get_heightmap_height(heightmap, row - 1, col)
    if height >= up_height:
        return False

    down_height = __get_heightmap_height(heightmap, row + 1, col)
    if height >= down_height:
        return False

    return True


def __get_heightmap_height(heightmap: HeightMap, row: int, col: int) -> int:
    """
    Returns the height of the heightmap at the given location.
    If the index is out ouf bounds, returns a large number.
    """
    if not 0 <= row < len(heightmap):
        return 1000000

    if not 0 <= col < len(heightmap[row]):
        return 1000000

    return heightmap[row][col]
