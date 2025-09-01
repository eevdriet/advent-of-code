import sys
from itertools import pairwise, permutations

import parse as ps

from aoc.util import timed

Name = str
Happiness = dict[tuple[Name, Name], int]


def parse(input: str) -> tuple[set[Name], Happiness]:
    names = set()
    happiness = {}

    for line in input.splitlines():
        name1, change, units, name2 = ps.search(
            "{} would {} {:d} happiness units by sitting next to {}.", line
        )
        sign = 1 if change == "gain" else -1

        names.add(name1)
        names.add(name2)
        happiness[(name1, name2)] = sign * units

    return names, happiness


def find_max_happiness(names: set[Name], happiness: Happiness) -> int:
    max_happiness = -sys.maxsize

    for arrangement in permutations(names):
        curr_happiness = 0

        # Compute the happiness of people sitting next to each other
        for name1, name2 in pairwise(arrangement):
            curr_happiness += happiness[(name1, name2)]
            curr_happiness += happiness[(name2, name1)]

        # Loop around the table
        if len(arrangement) > 2:
            curr_happiness += happiness[arrangement[0], arrangement[-1]]
            curr_happiness += happiness[arrangement[-1], arrangement[0]]

        max_happiness = max(curr_happiness, max_happiness)

    return max_happiness


def part1(names: set[Name], happiness: Happiness) -> int:
    return find_max_happiness(names, happiness)


def part2(names: set[Name], happiness: Happiness) -> int:
    MY_NAME = "..."

    for name in names:
        happiness[name, MY_NAME] = 0
        happiness[MY_NAME, name] = 0

    names.add(MY_NAME)

    return find_max_happiness(names, happiness)


if __name__ == "__main__":
    input = sys.stdin.read()
    names, happiness = parse(input)

    result1, elapsed = timed(part1, names, happiness)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, names, happiness)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
