import sys
from collections import defaultdict
from itertools import pairwise

from attrs import define, field

from aoc.io import read_file
from aoc.util import timed


@define
class Polymer:
    template: str
    pair_rules: dict[str, str]
    pair_counts: dict[str, int] = field(init=False)

    def __attrs_post_init__(self):
        self.pair_counts = defaultdict(int)

        for left, right in pairwise(self.template):
            pair = f"{left}{right}"
            self.pair_counts[pair] += 1

    def extend(self, n_steps: int = 1):
        for _ in range(n_steps):
            pair_counts = self.pair_counts.copy()

            for pair, count in self.pair_counts.items():
                # Remove the extended pair if found
                if pair not in self.pair_rules:
                    continue

                pair_counts[pair] -= count

                # Insert the new element and count towards neighboring pairs
                mid = self.pair_rules[pair]
                left, right = pair

                pair_counts[left + mid] += count
                pair_counts[mid + right] += count

            self.pair_counts = pair_counts

    def counts(self) -> dict[str, int]:
        result = defaultdict(int)

        # Count all left elements (ignore right to avoid double counting)
        for (left, _), count in self.pair_counts.items():
            result[left] += count

        # Count the very right element of the polymer of the last pair
        result[self.template[-1]] += 1

        return result


def parse(input: str) -> Polymer:
    template, rule_lines = input.split("\n\n")

    rules = {}

    for line in rule_lines.strip().splitlines():
        pair, elem = line.split(" -> ")
        rules[pair] = elem

    return Polymer(template, rules)


def part1(polymer: Polymer) -> int:
    polymer.extend(10)
    counts = polymer.counts()

    return max(counts.values()) - min(counts.values())


def part2(polymer: Polymer) -> int:
    polymer.extend(40)
    counts = polymer.counts()

    return max(counts.values()) - min(counts.values())


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2021, 14, "example")
    part1(parse(input))
