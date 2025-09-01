import sys
from collections import Counter

from aoc.util import adjacent8, timed

Coord = tuple[int, int]

def parse(input: str) -> dict[Coord, str]:
    area = {}

    for y, line in enumerate(input.splitlines()):
        for x, cell in enumerate(line):
            area[(x, y)] = cell

    return area


def simulate(area: dict[Coord, str], n_minutes: int) -> int:
    seen = {}
    minute = 0

    while minute < n_minutes:
        minute += 1
        new_area = dict(area)

        for coord, resource in area.items():
            new_resource = resource
            adjacent_counts = Counter(area[neighbor] for neighbor in adjacent8(coord) if neighbor in area)

            match resource:
                # Open becomes trees if >=3 neighbors are trees
                case '.' if adjacent_counts['|'] >= 3:
                    new_resource = '|'

                # Trees becomes a lumberyard if >=3 neighbors are lumberyards
                case '|' if adjacent_counts['#'] >= 3:
                    new_resource = '#'

                # Lumberyard becomes open if it wasn't ad
                case '#' if not (adjacent_counts['#'] >= 1 and adjacent_counts['|'] >= 1):
                    new_resource = '.'

            new_area[coord] = new_resource

        area = new_area

        # Try to detect a cycle to skip computations by keeping track of seen states
        state = "".join(area[coord] for coord in sorted(area.keys()))
        if state not in seen:
            seen[state] = minute
            continue

        # If seen before, we can skip as many cycles as still fit in the remaining minutes
        cycle_len = minute - seen[state]
        n_remaining = n_minutes - minute
        n_skipped_cycles = n_remaining // cycle_len

        minute += cycle_len * n_skipped_cycles

    resources = Counter(area.values())
    return resources['|'] * resources['#']

def part1(area: dict[Coord, str]) -> int:
    return simulate(area, 10)

def part2(area: dict[Coord, str]) -> int:
    return simulate(area, 1_000_000_000)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
