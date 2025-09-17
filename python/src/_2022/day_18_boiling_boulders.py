import sys
from collections import deque

from aoc.util import adjacent4, timed

Cube = tuple[int, int, int]


def parse(input: str) -> list[Cube]:
    cubes = []

    for line in input.splitlines():
        x, y, z = map(int, line.split(","))

        cube = x, y, z
        cubes.append(cube)

    return cubes


def part1(cubes: list[Cube]) -> int:
    cube_set = set(cubes)
    n_sides = 6 * len(cubes)

    for cube in cube_set:
        for neighbor in adjacent4(cube):
            if neighbor in cube_set:
                n_sides -= 1

    return n_sides


def part2(cubes: list[Cube]) -> int:
    cube_set = set(cubes)

    # Define the boundaries just outside of the cubes
    x_min = min(x for x, _, _ in cubes) - 1
    x_max = max(x for x, _, _ in cubes) + 1
    y_min = min(y for _, y, _ in cubes) - 1
    y_max = max(y for _, y, _ in cubes) + 1
    z_min = min(z for _, _, z in cubes) - 1
    z_max = max(z for _, _, z in cubes) + 1

    # Perform a flood-fill to determine all cubes on the outside
    outside = set()
    queue = deque([(x_min, y_min, z_min)])

    while queue:
        # Don't go back to an explored space on the outside or inside of the cubes
        cube = queue.popleft()

        if cube in outside:
            continue
        if cube in cube_set:
            continue

        # Don't go further (than 1 space from any cube) outside
        x, y, z = cube
        if not (x_min <= x <= x_max and y_min <= y <= y_max and z_min <= z <= z_max):
            continue

        outside.add(cube)

        for neighbor in adjacent4(cube):
            queue.append(neighbor)

    return sum(
        1 for cube in cubes for neighbor in adjacent4(cube) if neighbor in outside
    )


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
