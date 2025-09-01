import sys
from collections import defaultdict, deque

from aoc.util import timed

Coord = tuple[int, int]


def parse(input: str) -> list[Coord]:
    return [tuple(map(int, line.split(","))) for line in input.splitlines()]


def dist(coord1: Coord, coord2: Coord) -> int:
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


def part1(coords: list[Coord]) -> int:
    # Determine the boundaries of the coordinates
    max_x = max(coords, key=lambda coord: coord[0])[0]
    max_y = max(coords, key=lambda coord: coord[1])[1]

    coord_id_to_point = {
        coord_id: point for coord_id, point in enumerate(coords, start=1)
    }
    region_sizes = defaultdict(int)
    infinite_ids = set()

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            min_dists = sorted(
                [
                    (abs(r - x) + abs(c - y), coord_id)
                    for coord_id, (r, c) in coord_id_to_point.items()
                ]
            )

            if len(min_dists) == 1 or min_dists[0][0] != min_dists[1][0]:
                coord_id = min_dists[0][1]
                region_sizes[coord_id] += 1

                if x == 0 or x == max_x or y == 0 or y == max_y:
                    infinite_ids.add(coord_id)

    return max(
        size for coord_id, size in region_sizes.items() if coord_id not in infinite_ids
    )


def part2(coords: list[Coord], limit: int = 10_000) -> int:
    # Determine the boundaries of the coordinates
    max_x = max(coords, key=lambda coord: coord[0])[0]
    max_y = max(coords, key=lambda coord: coord[1])[1]

    size_shared_region = 0

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            size_shared_region += int(
                sum(abs(c - x) + abs(r - y) for c, r in coords) < limit
            )

    return size_shared_region


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
