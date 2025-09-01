import sys

from aoc.io import open_file
from aoc.util import timed

Grid = dict[complex, str]


def parse(input: str) -> tuple[Grid, complex]:
    grid = input.splitlines()
    start = complex(grid[0].index("|"), 0)

    return {
        complex(col, row): grid[row][col]
        for row in range(len(grid))
        for col in range(len(grid[row]))
        if grid[row][col] != " "
    }, start


def traverse_grid(grid: Grid, pos: complex) -> tuple[str, int]:
    seen = []
    dir = 0 + 1j
    n_steps = 0

    while pos in grid:
        n_steps += 1

        match grid[pos]:
            # Continue with straight lines
            case "|" | "-":
                pos += dir

            # On corners, turn to the side that is in bounds
            case "+":
                if (pos + (left := dir * 1j)) in grid:
                    pos += left
                    dir = left
                elif (pos + (right := dir * -1j)) in grid:
                    pos += right
                    dir = right

            case letter if letter.isalpha():
                seen.append(letter)
                pos += dir

    return "".join(seen), n_steps


def part1(grid: Grid, pos: complex) -> str:
    word, _ = traverse_grid(grid, pos)
    return word


def part2(grid: Grid, pos: complex) -> int:
    _, n_steps = traverse_grid(grid, pos)
    return n_steps


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, *parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    with open_file(2017, 19, name="example") as file:
        part1(*parse(file.read()))
