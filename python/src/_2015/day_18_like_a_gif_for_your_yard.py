import sys
from collections import defaultdict

from aoc.util import Point, adjacent8, timed


def parse(input: str) -> tuple[set[Point], int, int]:
    active_cells = {
        (row, col)
        for row, line in enumerate(input.splitlines())
        for col, state in enumerate(line.strip())
        if state == "#"
    }
    height = 1 + max(row for row, _ in active_cells)
    width = 1 + max(col for _, col in active_cells)

    return active_cells, height, width


def game_of_life(
    active_cells: set[Point],
    height: int,
    width: int,
    *,
    n_cycles: int,
    corners_stay_on: bool = False,
) -> int:
    for _ in range(n_cycles):
        neighbor_counts = defaultdict(int)

        for cell in active_cells:
            for neighbor in adjacent8(cell, bounds=(height, width)):
                neighbor_counts[neighbor] += 1

        stay_on = {cell for cell in active_cells if neighbor_counts[cell] in (2, 3)}
        turn_on = {
            cell
            for cell, count in neighbor_counts.items()
            if cell not in active_cells and count == 3
        }
        active_cells = stay_on | turn_on

        if corners_stay_on:
            active_cells |= {
                (0, 0),
                (0, width - 1),
                (height - 1, 0),
                (height - 1, width - 1),
            }

    return len(active_cells)


def part1(active_cells: set[Point], height: int, width: int) -> int:
    return game_of_life(
        active_cells, height, width, n_cycles=100, corners_stay_on=False
    )


def part2(active_cells: set[Point], height: int, width: int) -> int:
    return game_of_life(active_cells, height, width, n_cycles=100, corners_stay_on=True)


if __name__ == "__main__":
    input = sys.stdin.read()
    active_cells, height, width = parse(input)

    result1, elapsed = timed(part1, active_cells, height, width)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, active_cells, height, width)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
