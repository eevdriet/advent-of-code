import sys
from itertools import pairwise

from attrs import define

from aoc.util import timed


@define
class BoardingPass:
    row: int
    col: int

    @classmethod
    def parse(cls, text: str) -> "BoardingPass":
        def bin_search(splits: str, keep_left: str) -> int:
            n = 2 ** len(splits) - 1
            left = 0
            right = n

            for split in splits:
                mid = left + (right - left) // 2

                if split == keep_left:
                    right = mid
                else:
                    left = mid + 1

            return left

        row_splits, col_splits = text[:7], text[7:]
        row = bin_search(row_splits, "F")
        col = bin_search(col_splits, "L")

        return cls(row, col)

    @property
    def seat_id(self) -> int:
        return 8 * self.row + self.col


def parse(input: str) -> list[BoardingPass]:
    return [BoardingPass.parse(line) for line in input.splitlines()]


def part1(boarding_passes: list[BoardingPass]) -> int:
    return max(boarding_pass.seat_id for boarding_pass in boarding_passes)


def part2(boarding_passes: list[BoardingPass]) -> int:
    seat_ids = [boarding_pass.seat_id for boarding_pass in boarding_passes]
    seat_ids.sort()

    for prev_id, next_id in pairwise(seat_ids):
        if next_id - prev_id == 2:
            return prev_id + 1

    raise RuntimeError("No seat found with two adjacent ones")


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
