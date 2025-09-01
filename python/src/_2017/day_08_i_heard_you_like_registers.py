import operator
import sys
from collections import defaultdict

from aoc.util import timed

Instruction = list[str]


def parse(input: str) -> list[Instruction]:
    return [line.split() for line in input.splitlines()]


def execute(instructions: list[Instruction], part2: bool = False) -> int:
    registers = defaultdict(int)
    ops = {
        ">": operator.gt,
        ">=": operator.ge,
        "<": operator.lt,
        "<=": operator.le,
        "==": operator.eq,
        "!=": operator.ne,
        "inc": operator.add,
        "dec": operator.sub,
    }

    max_val = 0

    for instruction in instructions:
        # Get all relevant parts of the instruction
        reg, op, arg, _, other, other_op, other_arg = instruction

        # Ignore instruction if the `if` clause is invalid
        other_val = registers[other]
        if not ops[other_op](other_val, int(other_arg)):
            continue

        # Otherwise, update the register based on the operation
        val = ops[op](registers[reg], int(arg))
        max_val = max(val, max_val)
        registers[reg] = val

    return max_val if part2 else max(registers.values())


def part1(instructions: list[Instruction]) -> int:
    return execute(instructions, part2=False)


def part2(instructions: list[Instruction]) -> int:
    return execute(instructions, part2=True)


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
