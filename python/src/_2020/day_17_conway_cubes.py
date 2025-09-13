import sys
from collections import defaultdict
from collections.abc import Generator
from itertools import product

from aoc.util import timed

Cube2D = tuple[int, int]
Cube = tuple[int, ...]


def parse(input: str) -> set[Cube2D]:
    return {
        (x, y)
        for y, row in enumerate(input.splitlines())
        for x, cell in enumerate(row)
        if cell == "#"
    }


def neighbors(cube: Cube) -> Generator[Cube, None, None]:
    n_dims = len(cube)

    for diffs in product([-1, 0, 1], repeat=n_dims):
        if all(diff == 0 for diff in diffs):
            continue

        yield tuple(coord + diff for coord, diff in zip(cube, diffs))


def simulate(cubes2d: set[Cube2D], n_dims: int, n_cycles: int) -> int:
    # Create the cubes that are initially active for the right dimensionality
    active_cubes = {(x, y) + (0,) * (n_dims - 2) for x, y in cubes2d}

    for _ in range(n_cycles):
        # Count how many neighbors each active cube has
        neighor_counts = defaultdict(int)

        for cube in active_cubes:
            for neighbor in neighbors(cube):
                neighor_counts[neighbor] += 1

        # Determine which cubes will stay and turn on and update the active cubes
        stay_on = {cube for cube in active_cubes if neighor_counts[cube] in (2, 3)}
        turn_on = {
            cube
            for cube, count in neighor_counts.items()
            if cube not in active_cubes and count == 3
        }

        active_cubes = stay_on | turn_on

    return len(active_cubes)


def part1(cubes2d: set[Cube2D]) -> int:
    return simulate(cubes2d, 3, 6)


def part2(cubes2d: set[Cube2D]) -> int:
    return simulate(cubes2d, 4, 6)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
