import fileinput
from typing import List, Tuple

Position = Tuple[int, int]
Path = List[Position]

nums = [i for i in range(1, 10)]


class ExtendedRiskMap:
    def __init__(self, nums: List[List[int]], times: int):
        self.nums = nums
        self.source_size = len(nums)
        self.size = self.source_size * times

    def __getitem__(self, index: Position) -> int:
        i, j = index
        times_bottom = i // self.source_size
        times_right = j // self.source_size

        value = self.nums[i % self.source_size][j % self.source_size]
        idx = nums.index(value)
        new_idx = (idx + times_bottom + times_right) % len(nums)

        return nums[new_idx]

    @classmethod
    def from_input(self, times: int):
        return ExtendedRiskMap(
            [
                [int(n) for n in line.strip()]
                for line in fileinput.input()
            ],
            times
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
