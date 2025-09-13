import re
import sys
from collections import defaultdict

from attrs import define

from aoc.io import read_file
from aoc.util import timed

Bag = str


@define
class Baggage:
    _contain: dict[Bag, dict[Bag, int]]
    _contained_in: dict[Bag, set[Bag]]

    @classmethod
    def parse(cls, text: str) -> "Baggage":
        contain = defaultdict(dict)
        contained_in = defaultdict(set)

        for line in text.splitlines():
            match = re.match(r"^(.+) bags contain", line)
            outer_bag = match.group(1)

            for count, inner_bag in re.findall(
                r"(\d+) (.+?) bags?", line[match.end() :]
            ):
                contain[outer_bag][inner_bag] = int(count)
                contained_in[inner_bag].add(outer_bag)

        return cls(contain, contained_in)

    def contains(self, bag: Bag) -> dict[Bag, int]:
        return self._contain[bag]

    def contained_in(self, bag: Bag) -> set[Bag]:
        return self._contained_in[bag]


def parse(input: str) -> Baggage:
    return Baggage.parse(input)


def part1(baggage: Baggage) -> int:
    bags_holding_gold = set()

    def dfs(bag: Bag) -> None:
        for outer_bag in baggage.contained_in(bag):
            bags_holding_gold.add(outer_bag)
            dfs(outer_bag)

    dfs("shiny gold")
    return len(bags_holding_gold)


def part2(baggage: Baggage) -> int:
    def dfs(outer_bag: Bag) -> int:
        count = 0
        outer_items = baggage.contains(outer_bag)

        for inner_bag, inner_count in outer_items.items():
            count += inner_count
            count += inner_count * dfs(inner_bag)

        return count

    return dfs("shiny gold")


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2020, 7, "example1")
    part1(parse(input))
