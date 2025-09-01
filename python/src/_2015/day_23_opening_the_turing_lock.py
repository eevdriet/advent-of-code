import sys

from aoc.util import timed

Instruction = list[str]


def parse(input: str) -> list[Instruction]:
    return [line.replace(",", "").split() for line in input.splitlines()]


def execute(program: list[Instruction], registers: dict[str, int]) -> int:
    ip = 0

    while 0 <= ip < len(program):
        match program[ip]:
            # Register instructions
            case ("hlf", reg):
                registers[reg] //= 2
                ip += 1
            case ("tpl", reg):
                registers[reg] *= 3
                ip += 1
            case ("inc", reg):
                registers[reg] += 1
                ip += 1

            # Jump instructions
            case ("jmp", offset):
                ip += int(offset)
            case ("jie", reg, offset):
                ip += int(offset) if registers[reg] % 2 == 0 else 1
            case ("jio", reg, offset):
                ip += int(offset) if registers[reg] == 1 else 1
            case _:
                raise ValueError(f"Unknown instruction: {program[ip]}")

    return registers["b"]


def part1(program: list[Instruction]) -> int:
    return execute(program, {"a": 0, "b": 0})


def part2(program: list[Instruction]) -> int:
    return execute(program, {"a": 1, "b": 0})


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
