import fileinput
from typing import List, Set, Tuple

# Size of the octopuses grid
size = 10

OctopusesGrid = List[List[int]]
FlashesCount = int
FlashedOctopuses = Set[Tuple[int, int]]


def read_octopuses_grid() -> OctopusesGrid:
    return [
        [int(n) for n in line.strip()]
        for line in fileinput.input()
    ]


def simulate_octopuses_step(grid: OctopusesGrid) -> Tuple[OctopusesGrid, FlashesCount]:
    """
    During a single simulation step, the following occurs:

    - First, the energy level of each octopus increases by 1.

    - Then, any octopus with an energy level greater than 9 flashes. This
      increases the energy level of all adjacent octopuses by 1, including
      octopuses that are diagonally adjacent. If this causes an octopus to
      have an energy level greater than 9, it also flashes. This process
      continues as long as new octopuses keep having their energy level
      increased beyond 9. (An octopus can only flash at most once per step.)

    - Finally, any octopus that flashed during this step has its energy level
      set to 0, as it used all of its energy to flash.
    """
    flashing_octopuses = set()

    for i in range(size):
        for j in range(size):
            energy = grid[i][j]

            will_flash = energy == 9
            if will_flash:
                flashing_octopuses.add((i, j))

            grid[i][j] = (energy + 1) % 10

    __simulate_adjacent_flashes(grid, flashing_octopuses)

    return grid, __count_flashes(grid)


def __simulate_adjacent_flashes(
    grid: OctopusesGrid,
    flashed_octopuses: FlashedOctopuses
) -> OctopusesGrid:
    adjacent_flashes = set()

    for i, j in flashed_octopuses:
        grid, flashed = update_adjacent_positions(
            grid,
            i, j
        )
        adjacent_flashes.update(flashed)

    if adjacent_flashes:
        grid = __simulate_adjacent_flashes(
            grid,
            adjacent_flashes
        )

        return grid

    return grid


def update_adjacent_positions(
    grid: OctopusesGrid,
    i: int, j: int,
) -> Tuple[OctopusesGrid, FlashedOctopuses]:
    """
    Returns the grid with the adjacent positions of the given octopus updated and
    a set of any newly flashed octopuses.

    Already flashed octopuses can't be flashed again, neither their energy level
    incremented.
    """
    flashed_octopuses = set()

    for n, m in __get_adjacent_positions(i, j):
        energy = grid[n][m]
        has_flashed = energy == 0
        could_flash = energy == 9

        if has_flashed:
            continue

        if could_flash:
            flashed_octopuses.add((n, m))

        grid[n][m] = (energy + 1) % 10

    return grid, flashed_octopuses


def __get_adjacent_positions(i: int, j: int) -> List[Tuple[int, int]]:
    return filter(
        lambda xy: 0 <= xy[0] < size and 0 <= xy[1] < size,
        [
            (i - 1, j - 1),
            (i - 1, j),
            (i - 1, j + 1),
            (i, j - 1),
            (i, j + 1),
            (i + 1, j - 1),
            (i + 1, j),
            (i + 1, j + 1)
        ])


def __count_flashes(grid: OctopusesGrid) -> FlashesCount:
    flashes = 0

    for i in range(size):
        for j in range(size):
            if grid[i][j] == 0:
                flashes += 1

    return flashes


def __print_grid(grid: OctopusesGrid):
    for row in grid:
        print(' '.join(str(n) for n in row))