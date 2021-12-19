import fileinput
from typing import List, Tuple

Position = Tuple[int, int]
Path = List[Position]


class RiskMap:
    def __init__(self, nums: List[List[int]]):
        self.nums = nums
        self.size = len(nums)

    def __getitem__(self, index: Position) -> int:
        i, j = index
        return self.nums[i][j]

    @classmethod
    def from_input(self):
        return RiskMap(
            [
                [int(n) for n in line.strip()]
                for line in fileinput.input()
            ]
        )

    def nodes_reachable_from(self, pos: Position) -> Path:
        i, j = pos

        return filter(
            lambda ij: 0 <= ij[0] < self.size and 0 <= ij[1] < self.size,
            [
                (i - 1, j),
                (i, j + 1),
                (i + 1, j),
                (i, j - 1)
            ]
        )

    def print_path(self, path: Path):
        path_set = set(path)

        for i in range(self.size):
            for j in range(self.size):
                cell = self[(i, j)]

                if (i, j) in path_set:
                    print(f'[{cell}]', end='')
                else:
                    print(f' {cell} ', end='')
            print()
