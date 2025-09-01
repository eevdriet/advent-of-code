import sys
from itertools import count

import parse as ps
from attrs import define

from aoc.alg import find_min_x
from aoc.util import timed


@define
class Disc:
    n_positions: int
    start: int

    @classmethod
    def parse(cls, text: str) -> "Disc":
        _, n, start = ps.parse(
            "Disc #{:d} has {:d} positions; at time=0, it is at position {:d}.", text
        )
        return cls(n, start)


def parse(input: str) -> list[Disc]:
    return [Disc.parse(line) for line in input.splitlines()]


def find_earliest_time(discs: list[Disc]) -> int:
    for time in count(0):
        is_possible = True

        for offset, disc in enumerate(discs, 1):
            pos = (offset + disc.start + time) % disc.n_positions
            if pos != 0:
                is_possible = False
                break

        if is_possible:
            return time

    # Should not get here
    return -1


def part1(discs: list[Disc]) -> int:
    return find_earliest_time(discs)


def part2(discs: list[Disc]) -> int:
    return find_earliest_time(discs + [Disc(11, 0)])


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(find_earliest_time, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
