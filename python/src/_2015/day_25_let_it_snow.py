import sys

import parse as ps

from aoc.util import timed


def parse(input: str) -> tuple[int, int]:
    return ps.parse(
        "To continue, please consult the code grid in the manual.  Enter the code at row {:d}, column {:d}.",
        input,
    )


def part1(row: int, col: int) -> int:
    n_diagonals = row + col - 2
    n_steps = col + n_diagonals * (n_diagonals + 1) // 2

    return (20151125 * pow(252533, n_steps - 1, 33554393)) % 33554393


def part1_iter(end_row: int, end_col: int) -> int:
    val = 20151125

    row = 1
    col = 1

    while row != end_row or col != end_col:
        # Move diagonally up and right until the first row
        if row > 1:
            row -= 1
            col += 1

        # Then start a new diagonal
        else:
            row = col + 1
            col = 1

        val = (val * 252533) % 33554393

    return val


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")
