import sys
from collections import namedtuple

from attrs import define

from aoc.io import read_file
from aoc.util import timed
from aoc.util.re import find_nums

Coord = namedtuple("Coord", ["x", "y"])


@define
class Scanner:
    location: Coord
    closest_beacon: Coord

    @property
    def reach(self) -> int:
        x_scanner, y_scanner = self.location
        x_beacon, y_beacon = self.closest_beacon

        return abs(x_scanner - x_beacon) + abs(y_scanner - y_beacon)

    def dist(self, coord: Coord) -> int:
        return abs(self.location.x - coord.x) + abs(self.location.y - coord.y)

    def x_range(self, y: int) -> range:
        width = abs(self.location.y - y)
        if width > self.reach:
            return range(0, 0)

        return range(
            self.location.x - (self.reach - width),
            self.location.x + (self.reach - width) + 1,
        )

    def y_range(self, x: int) -> range:
        width = abs(self.location.x - x)
        if width > self.reach:
            return range(0, 0)

        return range(
            self.location.y - (self.reach - width),
            self.location.y + (self.reach - width) + 1,
        )


def parse(input: str) -> list[Scanner]:
    scanners = []

    for line in input.splitlines():
        x_scanner, y_scanner, x_beacon, y_beacon = find_nums(line)

        location = Coord(x_scanner, y_scanner)
        beacon = Coord(x_beacon, y_beacon)

        scanner = Scanner(location, beacon)
        scanners.append(scanner)

    return scanners


def part1(scanners: list[Scanner], y: int = 2_000_000) -> int:
    line_beacons = set()
    line_non_beacons = set()

    for scanner in scanners:
        if scanner.closest_beacon.y == y:
            line_beacons.add(scanner.closest_beacon.x)
        if scanner.location.y == y:
            line_beacons.add(scanner.location.x)

        xs = scanner.x_range(y)
        for x in xs:
            line_non_beacons.add(x)

    return len(line_non_beacons - line_beacons)


def part2(scanners: list[Scanner], limit: int = 4_000_000) -> int:
    for scanner in scanners:
        # candidate points lie exactly one step outside the scanner's reach
        reach = scanner.reach + 1
        x0, y0 = scanner.location

        for dx in range(-reach, reach + 1):
            dy = reach - abs(dx)

            # handle dy == 0 explicitly (to avoid duplicate/skipped coords)
            if dy == 0:
                candidates = [Coord(x0 + dx, y0)]
            else:
                candidates = [Coord(x0 + dx, y0 + dy), Coord(x0 + dx, y0 - dy)]

            for coord in candidates:
                # must lie inside search area
                if not (0 <= coord.x < limit and 0 <= coord.y < limit):
                    continue

                # check if outside all scanners' reach
                if all(
                    other_scanner.dist(coord) > other_scanner.reach
                    for other_scanner in scanners
                ):
                    # tuning frequency formula
                    return coord.x * 4_000_000 + coord.y

    raise RuntimeError("No valid location found")


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    example = read_file(2022, 15, "example")
    part2(parse(example), 20)
