from math import prod
from typing import List


def read_num(grid: List[str], row: int, col: int) -> int:
    """Read a number from the grid starting at (row, col)

    :param grid: Grid to read number from
    :param row: Starting row of the number
    :param col: Starting column of the number
    :return: Number read from the grid
    """
    num_str = ""

    while col < len(grid[row]) and grid[row][col].isdigit():
        num_str += grid[row][col]
        col += 1

    return int(num_str)


def part1(grid: List[str]) -> int:
    # Store which numbers are not adjacent to a symbol
    seen = set()

    # Go through each cell
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            # Ignore numbers or blanks
            if ch.isdigit() or ch == ".":
                continue

            # Look in all directions from a symbol
            for cr in [r - 1, r, r + 1]:
                for cc in [c - 1, c, c + 1]:
                    # Skip if the adjacent cell is not valid/a number
                    if not (0 <= cr < len(grid)) or not (0 <= cc < len(grid[cr])):
                        continue
                    if not grid[cr][cc].isdigit():
                        continue

                    # Iterate until the starting column of the number in the grid
                    while cc > 0 and grid[cr][cc - 1].isdigit():
                        cc -= 1

                    seen.add((cr, cc))

    return sum(read_num(grid, row, col) for row, col in seen)


def part2(grid: List[str]) -> int:
    total = 0

    for r, row in enumerate(grid):
        for col, ch in enumerate(row):
            # Ignore non-gears
            if ch != "*":
                continue

            seen = set()

            for cr in [r - 1, r, r + 1]:
                for cc in [col - 1, col, col + 1]:
                    if not (0 <= cr < len(grid)) or not (0 <= cc < len(grid[cr])):
                        continue
                    if not grid[cr][cc].isdigit():
                        continue

                    while cc > 0 and grid[cr][cc - 1].isdigit():
                        cc -= 1

                    seen.add((cr, cc))

            if len(seen) != 2:
                continue

            total += prod(read_num(grid, row, col) for row, col in seen)

    return total


def main():
    grid = open("data/3.input").read().splitlines()

    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")


if __name__ == "__main__":
    main()
