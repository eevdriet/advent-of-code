import re
import sys
from enum import Enum, auto

from aoc.util import timed

Instruction = tuple[str, int]


class Status(Enum):
    HALTED = auto()
    INFINITE_LOOP = auto()


def parse(input: str) -> list[Instruction]:
    instructions = []

    for line in input.splitlines():
        match = re.match(r"(nop|acc|jmp) ([+-]\d+)", line)
        op, val = match.groups()

        instructions.append((op, int(val)))

    return instructions


def run(program: list[Instruction]) -> tuple[int, Status]:
    executed = set()

    ip = 0
    acc = 0

    while ip not in executed and ip in range(len(program)):
        executed.add(ip)
        instruction = program[ip]

        match instruction:
            case ("acc", val):
                acc += val
                ip += 1
            case ("jmp", jump):
                ip += jump
            case ("nop", _):
                ip += 1
            case _:
                raise ValueError(f"Unexpected instruction '{instruction}' found")

    status = Status.INFINITE_LOOP if ip in executed else Status.HALTED
    return acc, status


def part1(program: list[Instruction]) -> int:
    acc, status = run(program)
    assert status == Status.INFINITE_LOOP

    return acc


def part2(program: list[Instruction]) -> int:
    for idx, (op, val) in enumerate(program):
        # Ignore instructions that shouldn't be replaced
        if op not in {"jmp", "nop"}:
            continue

        # Replace 'jmp' <-> 'nop' instruction
        new_op = "jmp" if op == "nop" else "nop"
        new_program = program.copy()
        new_program[idx] = new_op, val

        # Verify the program halted given the replaced instruction
        acc, status = run(new_program)

        if status == Status.HALTED:
            return acc

    raise RuntimeError(
        "Couldn't replace a 'jmp' or 'nop' instruction in the program to make it halt"
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
