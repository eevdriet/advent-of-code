import re
import sys
from collections import Counter
from typing import Optional

from aoc.io import open_file
from aoc.util import timed


class ProgramNode:
    def __init__(self, name: str, weight: int, parent: Optional["ProgramNode"] = None):
        self.name = name
        self.weight = weight

        self.parent = parent
        self.children = []


def parse(input: str) -> list[ProgramNode]:
    # Store the nodes by name for easy access
    programs = {}
    lines = {}

    def process(line: str) -> ProgramNode:
        if not (match := re.match(r"(\w+) \((\d+)\)(?: -> (.*))?", line)):
            assert ValueError(f"Cannot create program from line '{line}'")

        # Create program from its name and weight
        name, weight, children = match.groups()
        if name in programs:
            return programs[name]

        program = ProgramNode(name, int(weight))
        programs[name] = program

        # If the program has children, attach those
        if children:
            for child in children.split(", "):
                node = programs[child] if child in programs else process(lines[child])

                program.children.append(node)
                node.parent = program

        return program

    # Pre-process lines so we can recursively handle them
    for line in input.splitlines():
        name, *_ = line.split()
        lines[name] = line

    # Create the program nodes one by one
    return [process(line) for line in input.splitlines()]


def part1(programs: list[ProgramNode]) -> str:
    # Traverse up through the programs until the root
    node = programs[0]

    while node.parent:
        node = node.parent

    return node.name


def part2(programs: list[ProgramNode]) -> int:
    # Find the root to balance
    root_name = part1(programs)
    root = next((p for p in programs if p.name == root_name))

    shift_weight = -1

    def total_weight(node: ProgramNode):
        nonlocal shift_weight
        weights = [total_weight(child) for child in node.children]

        # All nodes have the same weight: do nothing
        if shift_weight == -1 and len(set(weights)) > 1:
            (good_weight, _), (bad_weight, _) = Counter(weights).most_common(2)
            bad_child = weights.index(bad_weight)

            shift_weight = node.children[bad_child].weight + good_weight - bad_weight

        return node.weight + sum(weights)

    total_weight(root)
    return shift_weight


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    with open_file(2017, 7, name="example") as file:
        lines = parse(file.read())

    part2(lines)
