import operator
import sys
from typing import Callable

from aoc.util import timed

OPERATORS: dict[str, Callable] = {
    "EQ": lambda x: x,
    "NOT": lambda x: ~x,
    "AND": operator.and_,
    "OR": operator.or_,
    "LSHIFT": operator.lshift,
    "RSHIFT": operator.rshift,
}

Instructions = dict[str, list[str | int]]


def parse(input: str) -> Instructions:
    instructions = {}

    for line in input.splitlines():
        ops = line.split()
        wire = ops[-1]

        match len(ops):
            case 3:
                instructions[wire] = ("EQ", ops[0])
            case 4:
                instructions[wire] = (ops[0], ops[1])
            case _:
                instructions[wire] = (ops[1], ops[0], ops[2])

    return instructions


def part1(instructions: Instructions) -> ...:
    signals = {}
    return find_signal("a", instructions, signals)


def part2(instructions: Instructions) -> ...:
    # Find the original signal for A
    signals = {}
    a = find_signal("a", instructions, signals=signals)

    # Set the signal for B to the found value and reset derivations
    instructions["b"] = ["EQ", a]
    signals.clear()

    # Once again find the signal for A
    return find_signal("a", instructions, signals=signals)


def find_signal(wire: str, instructions: Instructions, signals: dict = {}) -> int:
    # Retrieve cached result
    if wire in signals:
        return signals[wire]

    # Signal for literal values is the value itself
    try:
        return int(wire)
    except ValueError:
        pass

    # Signal for operations is recursively found through its arguments
    op_str, *arg_strs = instructions[wire]

    op = OPERATORS[op_str]
    args = [find_signal(arg_str, instructions, signals) for arg_str in arg_strs]

    # Cache the signal and return it
    signals[wire] = op(*args)
    return signals[wire]


def main():
    input = sys.stdin.read()
    instructions = parse(input)

    result1, elapsed = timed(part1, instructions)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, instructions)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
