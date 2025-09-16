import re
import sys
from math import prod
from typing import Literal

from attrs import define

from aoc.util import timed

Instruction = tuple[Literal["on"] | Literal["off"], "NDRange"]


@define
class NDRange:
    ranges: list[range]

    @property
    def dim(self):
        return len(self.ranges)

    @property
    def size(self):
        return prod(len(r) for r in self.ranges)

    def intersects(self, other: "NDRange") -> bool:
        return all(
            not (range1.stop <= range2.start or range2.stop <= range1.start)
            for range1, range2 in zip(self.ranges, other.ranges)
        )

    def intersection(self, b: "NDRange") -> "NDRange | None":
        new_ranges = []

        for range1, range2 in zip(self.ranges, b.ranges):
            start = max(range1.start, range2.start)
            stop = min(range1.stop, range2.stop)

            if start >= stop:
                return None

            new_ranges.append(range(start, stop))

        return NDRange(new_ranges)

    def subtract(self, cutter: "NDRange") -> list["NDRange"]:
        intersection = self.intersection(cutter)
        if intersection is None:
            return [self]

        result: list[NDRange] = []

        def helper(dim: int, prefix: list[range]):
            if dim == self.dim:
                candidate = NDRange(prefix)
                if candidate != intersection:
                    result.append(candidate)

                return

            ranges = self.ranges[dim]
            iranges = intersection.ranges[dim]

            # left slice
            if ranges.start < iranges.start:
                helper(dim + 1, prefix + [range(ranges.start, iranges.start)])

            # middle slice
            helper(dim + 1, prefix + [range(iranges.start, iranges.stop)])

            # right slice
            if iranges.stop < ranges.stop:
                helper(dim + 1, prefix + [range(iranges.stop, ranges.stop)])

        helper(0, [])
        return result


def parse(input: str) -> list[Instruction]:
    instructions = []
    dr = r"(-?\d+)"

    for line in input.splitlines():
        match = re.match(
            rf"(on|off) x={dr}\.\.{dr},y={dr}\.\.{dr},z={dr}\.\.{dr}", line
        )
        if not match:
            raise ValueError(f"Couldn't parse instruction from '{line}'")

        typ, x_min, x_max, y_min, y_max, z_min, z_max = match.groups()

        x_range = range(int(x_min), int(x_max) + 1)
        y_range = range(int(y_min), int(y_max) + 1)
        z_range = range(int(z_min), int(z_max) + 1)

        instruction = typ, NDRange([x_range, y_range, z_range])
        instructions.append(instruction)

    return instructions


def apply_instructions(instructions: list[Instruction]) -> list[NDRange]:
    active: list[NDRange] = []

    for typ, cube in instructions:
        new_active: list[NDRange] = []
        if typ == "on":
            # subtract existing cubes from the new cube, keep leftovers
            leftovers = [cube]
            for act in active:
                next_leftovers = []
                for lf in leftovers:
                    next_leftovers.extend(lf.subtract(act))
                leftovers = next_leftovers
            new_active = active + leftovers
        else:  # "off"
            for act in active:
                new_active.extend(act.subtract(cube))

        active = new_active

    return active


def part1(instructions: list[Instruction]) -> int:
    region = NDRange([range(-50, 50 + 1)] * 3)
    limited = []

    for typ, ndrange in instructions:
        if ndrange.intersects(region):
            limited += [(typ, ndrange.intersection(region))]

    actives = apply_instructions(limited)
    return sum(active.size for active in actives)


def part2(instructions: list[Instruction]) -> int:
    actives = apply_instructions(instructions)
    return sum(active.size for active in actives)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
