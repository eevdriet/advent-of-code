import sys

from attrs import define, field

from aoc.io import read_file
from aoc.util import timed


@define
class Bingo:
    __MASK = 2**5 - 1

    id: int
    nums: list[int]
    winning_num: int = field(default=None)

    _rows: list[int] = field(factory=lambda: [0 for _ in range(5)])
    _cols: list[int] = field(factory=lambda: [0 for _ in range(5)])

    @property
    def unmarked(self) -> list[int]:
        return [
            num
            for pos, num in enumerate(self.nums)
            if not self._rows[pos // 5] & 1 << (pos % 5)
        ]

    def mark(self, num: int):
        try:
            idx = self.nums.index(num)
        except ValueError:
            return

        # Mark the number in the rows and columns
        row, col = divmod(idx, 5)

        self._rows[row] |= 1 << col
        self._cols[col] |= 1 << row

    def has_won(self) -> bool:
        if any(not row ^ self.__MASK for row in self._rows):
            return True
        if any(not col ^ self.__MASK for col in self._cols):
            return True

        return False


def parse(input: str) -> tuple[list[int], list[Bingo]]:
    nums_text, *board_texts = input.split("\n\n")
    nums = [int(num) for num in nums_text.strip().split(",")]

    boards = []
    for id, board_text in enumerate(board_texts):
        board_nums = [int(num) for num in board_text.strip().split()]

        board = Bingo(id, board_nums)
        boards.append(board)

    return nums, boards


def simulate(nums: list[int], boards: list[Bingo]) -> list[Bingo]:
    winners = []

    for num in nums:
        for board in boards:
            if board.has_won():
                continue

            board.mark(num)

            if board.has_won():
                board.winning_num = num
                winners.append(board)

    return winners


def part1(nums: list[int], boards: list[Bingo]) -> int:
    first_winner, *_ = simulate(nums, boards)

    return sum(first_winner.unmarked) * first_winner.winning_num


def part2(nums: list[int], boards: list[Bingo]) -> int:
    *_, last_winner = simulate(nums, boards)

    return sum(last_winner.unmarked) * last_winner.winning_num


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, *parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2021, 4, "example")
    part1(*parse(input))
