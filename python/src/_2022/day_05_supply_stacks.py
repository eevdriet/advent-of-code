import re
import sys
from collections import defaultdict

from aoc.util import timed

Stack = list[str]
Instruction = tuple[int, int, int]


def parse(input: str) -> tuple[list[Stack], list[Instruction]]:
    stack_text, instructions_text = input.split("\n\n")

    # Parse the stacks
    stacks = defaultdict(list)
    for line in stack_text.splitlines():
        for match in re.finditer(r"\[(\w)\]", line):
            idx = match.start() // 4
            crate = match.group(1)

            stacks[idx].append(crate)

    # Reverse all stacks' contents
    for idx in stacks:
        stacks[idx].reverse()

    # Parse the instructions (move to 0-based indexing)
    instructions = []

    for line in instructions_text.splitlines():
        amount, src, dst = map(int, re.findall(r"\d+", line))
        instructions.append((amount, src - 1, dst - 1))

    return [stacks[idx] for idx in sorted(stacks)], instructions


def part1(stacks: list[Stack], instructions: list[Instruction]) -> str:
    for amount, src, dst in instructions:
        crates = [stacks[src].pop() for _ in range(amount)]
        stacks[dst] += crates

    return "".join(stack[-1] for stack in stacks)


def part2(stacks: list[Stack], instructions: list[Instruction]) -> str:
    for amount, src, dst in instructions:
        moved = stacks[src][-amount:]
        remaining = stacks[src][:-amount]

        stacks[src] = remaining
        stacks[dst] += moved

    return "".join(stack[-1] for stack in stacks)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, *parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
