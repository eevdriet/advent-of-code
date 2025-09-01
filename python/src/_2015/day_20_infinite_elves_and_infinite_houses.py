import sys
from typing import Optional

from aoc.util import timed


def parse(input: str) -> int:
    return int(input)


def lowest_house(
    num: int, *, n_presents_per_house: int, max_n_houses: Optional[int] = None
) -> int:
    # Determine how many presents should be delivered
    target = num // 10
    presents = [0] * (target + 1)

    for elf in range(1, target + 1):
        houses = range(elf, target + 1, elf)

        for n_houses, house in enumerate(houses):
            if max_n_houses is not None and n_houses > max_n_houses:
                break

            presents[house] += n_presents_per_house * elf

    return next(
        (house for house, n_presents in enumerate(presents) if n_presents >= num),
        -1,
    )


def part1(n_presents: int) -> int:
    return lowest_house(n_presents, n_presents_per_house=10)


def part2(n_presents: int) -> int:
    return lowest_house(n_presents, n_presents_per_house=11, max_n_houses=50)


if __name__ == "__main__":
    input = sys.stdin.read()
    n_presents = parse(input)

    result1, elapsed = timed(part1, n_presents)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, n_presents)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
