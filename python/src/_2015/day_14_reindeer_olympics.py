import sys
from collections import defaultdict

import parse as ps

from aoc.util import timed

N_SECONDS = 2503


class Reindeer:
    def __init__(
        self, name: str, km_per_second: int, n_fly_seconds: int, n_rest_seconds: int
    ):
        self.name = name

        self.km_per_second = km_per_second
        self.n_fly_seconds = n_fly_seconds
        self.n_rest_seconds = n_rest_seconds

    @classmethod
    def parse(cls, line: str):
        name, km_per_second, n_fly_seconds, n_rest_seconds = ps.search(
            "{} can fly {:d} km/s for {:d} seconds, but then must rest for {:d} seconds.",
            line,
        )

        return Reindeer(name, km_per_second, n_fly_seconds, n_rest_seconds)

    def __hash__(self):
        return hash(self.name)

    def distance_traveled(self, n_seconds: int) -> int:
        n_flown_seconds = 0

        n_full_flights = n_seconds // (self.n_fly_seconds + self.n_rest_seconds)
        n_flown_seconds += n_full_flights * self.n_fly_seconds
        n_flown_seconds += min(
            n_seconds % (self.n_fly_seconds + self.n_rest_seconds), self.n_fly_seconds
        )

        return self.km_per_second * n_flown_seconds


def parse(input: str) -> list[Reindeer]:
    return [Reindeer.parse(line) for line in input.splitlines()]


def part1(reindeers: list[Reindeer], n_seconds: int) -> int:
    return max(reindeer.distance_traveled(n_seconds) for reindeer in reindeers)


def part2(reindeers: list[Reindeer], n_seconds: int) -> int:
    points: dict[Reindeer, int] = defaultdict(lambda: 0)

    for second in range(1, n_seconds + 1):
        winner = max(reindeers, key=lambda reindeer: reindeer.distance_traveled(second))
        points[winner] += 1

    return max(points.values())


if __name__ == "__main__":
    input = sys.stdin.read()
    reindeers = parse(input)

    result1, elapsed = timed(part1, reindeers, N_SECONDS)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, reindeers, N_SECONDS)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
