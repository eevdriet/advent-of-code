import sys
from functools import reduce

from _2019.intcode import IntCode, asciify
from aoc.util import timed


def parse(input: str) -> list[int]:
    return [int(num) for num in input.split(",")]


def jump_bot(memory: list[int], instructions: list[str]) -> int:
    program = IntCode(memory)
    inputs = reduce(
        lambda acc, instruction: acc + asciify([instruction]), instructions, []
    )
    outputs = program.run(inputs)

    return outputs[-1]


def part1(memory: list[int]) -> int:
    return jump_bot(
        memory, ["NOT A J", "NOT B T", "OR T J", "NOT C T", "OR T J", "AND D J", "WALK"]
    )


def part2(memory: list[int]) -> int:
    return jump_bot(
        memory,
        [
            "OR A T",
            "AND B T",
            "AND C T",
            "NOT T J",
            "AND D J",
            "OR H T",
            "OR E T",
            "AND T J",
            "RUN",
        ],
    )


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
