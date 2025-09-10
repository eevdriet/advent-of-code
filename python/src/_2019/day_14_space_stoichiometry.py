import sys
from collections import defaultdict
from math import ceil

from attrs import define

from aoc.io import read_file
from aoc.util import timed

Reaction = tuple[int, list[tuple[str, int]]]


@define
class NanoFactory:
    reactions: dict[str, Reaction]

    @classmethod
    def parse(cls, input: str) -> "NanoFactory":
        reactions = {}

        for line in input.splitlines():
            inputs, output = line.split(" => ")
            out_quantity, out_chem = output.split()

            in_chems = []

            for input in inputs.split(", "):
                in_quantity, in_chem = input.split()
                in_chems.append((in_chem, int(in_quantity)))

            reactions[out_chem] = int(out_quantity), in_chems

        return cls(reactions)

    def is_terminal(self, chem: str) -> bool:
        return len(self.reactions[chem]) == 1

    def produce_from_ore(
        self, chem: str, quantity: int, chemicals: dict[str, int]
    ) -> int:
        # Produce ORE directly
        if chem == "ORE":
            return quantity

        out_quantity, inputs = self.reactions[chem]

        # No (additional) ore has to be used based on available chemicals
        if chemicals[chem] >= quantity:
            chemicals[chem] -= quantity
            return 0

        # Use everything already available
        quantity -= chemicals[chem]
        chemicals[chem] = 0

        # For the remainder, produce as much as still needed
        n_batches = ceil(quantity / out_quantity)
        ore_needed = 0

        for in_chem, in_quantity in inputs:
            ore_needed += self.produce_from_ore(
                in_chem, in_quantity * n_batches, chemicals
            )

        chemicals[chem] += (n_batches * out_quantity) - quantity

        return ore_needed


def parse(input: str) -> NanoFactory:
    return NanoFactory.parse(input)


def part1(factory: NanoFactory) -> int:
    return factory.produce_from_ore("FUEL", 1, defaultdict(int))


def part2(factory: NanoFactory) -> int:
    MAX_ORE_QUANTITY = 1_000_000_000_000
    max_fuel = 1

    # Use a binary search to find the maximum fuel amount to produce
    left = 0
    right = MAX_ORE_QUANTITY

    while left <= right:
        mid = (right - left) // 2 + left
        ore_quantity = factory.produce_from_ore("FUEL", mid, defaultdict(int))

        if ore_quantity <= MAX_ORE_QUANTITY:
            max_fuel = mid
            left = mid + 1
        else:
            right = mid - 1

    return max_fuel


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2019, 14, "example1")
    part1(parse(input))
