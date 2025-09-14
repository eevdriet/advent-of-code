import re
import sys
from collections import Counter

from attrs import define, field

from aoc.util import minmax, timed

Coord = tuple[int, int]
Segment = tuple[Coord, Coord]


@define
class Vents:
    counts: Counter[Coord] = field(factory=lambda: Counter())

    def scan(self, segment: Segment, include_diagonal: bool = True):
        # Break down the segment and order the coordinates
        (x1, y1), (x2, y2) = segment

        x_min, x_max = minmax(x1, x2)
        y_min, y_max = minmax(y1, y2)

        # Count which vents are covered
        if x1 == x2:
            self.counts.update((x1, y) for y in range(y_min, y_max + 1))
        elif y1 == y2:
            self.counts.update((x, y1) for x in range(x_min, x_max + 1))

        elif include_diagonal:
            x_range = range(x1, x2 + 1) if x2 > x1 else reversed(range(x2, x1 + 1))
            y_range = range(y1, y2 + 1) if y2 > y1 else reversed(range(y2, y1 + 1))

            self.counts.update((x, y) for x, y in zip(x_range, y_range))


def parse(input: str) -> list[Segment]:
    segments = []

    for line in input.splitlines():
        x1, y1, x2, y2 = map(int, re.findall(r"(-?\d+)", line))

        segment = (x1, y1), (x2, y2)
        segments.append(segment)

    return segments


def part1(segments: list[Segment]) -> int:
    vents = Vents()

    for segment in segments:
        vents.scan(segment, include_diagonal=False)

    return sum(count >= 2 for count in vents.counts.values())


def part2(segments: list[Segment]) -> int:
    vents = Vents()

    for segment in segments:
        vents.scan(segment, include_diagonal=True)

    return sum(count >= 2 for count in vents.counts.values())


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
