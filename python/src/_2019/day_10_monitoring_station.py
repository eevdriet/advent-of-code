import sys
from collections import defaultdict
from math import atan2, gcd, pi

from aoc.io import read_file
from aoc.util import timed

Coord = tuple[int, int]


def parse(input: str) -> set[Coord]:
    return {
        (x, y)
        for y, row in enumerate(input.splitlines())
        for x, cell in enumerate(row)
        if cell == "#"
    }


def get_dir(coord1: Coord, coord2: Coord) -> Coord:
    x1, y1 = coord1
    x2, y2 = coord2

    dx = x2 - x1
    dy = y2 - y1
    n = gcd(dx, dy)

    return dx // n, dy // n


def place_station(asteroids: set[Coord]) -> tuple[Coord, int]:
    def count_visible(station: Coord) -> int:
        directions = set()

        for asteroid in asteroids - {station}:
            dir = get_dir(station, asteroid)
            directions.add(dir)

        return len(directions)

    max_n_asteroids = 0
    max_coord = (0, 0)

    for asteroid in asteroids:
        n_asteroids = count_visible(asteroid)
        if n_asteroids > max_n_asteroids:
            max_n_asteroids = n_asteroids
            max_coord = asteroid

    return max_coord, max_n_asteroids


def part1(asteroids: set[Coord]) -> int:
    _, n_asteroids = place_station(asteroids)
    return n_asteroids


def vaporize_asteroids(station: Coord, asteroids: set[Coord]) -> list[Coord]:
    # Collect all asteroids in terms of their direction to the station and sort them on distance
    groups = defaultdict(list)

    for asteroid in asteroids - {station}:
        dx = asteroid[0] - station[0]
        dy = asteroid[1] - station[1]

        dir = get_dir(station, asteroid)
        dist = dx**2 + dy**2
        groups[dir].append((dist, asteroid))

    for group in groups.values():
        group.sort()

    # Order all (other) asteroids in terms of their angle and distance to the station
    def angle(dir: tuple[int, int]) -> float:
        dx, dy = dir
        return (atan2(dx, -dy) + 2 * pi) % (2 * pi)

    directions = sorted(groups.keys(), key=angle)
    order = []

    while groups:
        for direction in directions:
            if direction in groups and groups[direction]:
                _, asteroid = groups[direction].pop(0)
                order.append(asteroid)
                if not groups[direction]:
                    del groups[direction]

        directions = [dir for dir in directions if dir in groups]

    return order


def part2(asteroids: set[Coord]) -> int:
    # Place the station and determine its coordinate
    station, _ = place_station(asteroids)
    vaporized = vaporize_asteroids(station, asteroids)

    assert len(vaporized) >= 200

    nth_asteroid = vaporized[199]
    x, y = nth_asteroid

    return 100 * x + y


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2019, 10, "example1")
    part1(*parse(input))
