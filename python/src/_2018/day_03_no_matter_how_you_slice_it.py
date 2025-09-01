import sys
from collections import defaultdict

import parse as ps
from attrs import define

from aoc.io import open_file
from aoc.util import timed


@define
class Claim:
    id: int

    left: int
    top: int

    width: int
    height: int

    @classmethod
    def parse(cls, line: str) -> "Claim":
        vals = ps.parse("#{:d} @ {:d},{:d}: {:d}x{:d}", line)
        return cls(*vals)

    def __hash__(self):
        return hash(self.id)


def parse(input: str) -> list[Claim]:
    return [Claim.parse(line) for line in input.splitlines()]


def part1(claims: list[Claim]) -> int:
    claimed = defaultdict(int)

    for claim in claims:
        row = claim.top
        col = claim.left

        for dr in range(claim.height):
            for dc in range(claim.width):
                pos = row + dr, col + dc
                claimed[pos] += 1

    return sum(1 for count in claimed.values() if count > 1)


def part2(claims: list[Claim]) -> int:
    claimed = {}
    candidates = set(claims)

    for claim in claims:
        row = claim.top
        col = claim.left

        for dr in range(claim.height):
            for dc in range(claim.width):
                pos = row + dr, col + dc

                if pos in claimed:
                    candidates.discard(claim)
                    candidates.discard(claimed[pos])

                claimed[pos] = claim

    assert len(candidates) == 1
    return list(candidates)[0].id


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    with open_file(2018, 3, "example") as file:
        part1(parse(file.read()))
