import sys
from collections import defaultdict

from aoc.util import timed

Instruction = list[str]


def parse(input: str) -> list[Instruction]:
    return [line.split() for line in input.strip().splitlines()]


def execute(
    program: list[Instruction], registers: defaultdict = defaultdict(int)
) -> int:
    ip = 0

    def get_val(x: str) -> int:
        return registers[x] if x.isalpha() else int(x)

    while 0 <= ip < len(program):
        match program[ip]:
            case ("cpy", src, dst):
                val = get_val(src)
                registers[dst] = val
            case ("inc", reg):
                registers[reg] += 1
            case ("dec", reg):
                registers[reg] -= 1
            case ("jnz", num, jump):
                if get_val(num) != 0:
                    ip += int(jump)
                    continue

        ip += 1

    return registers["a"]


def part1(instructions: list[Instruction]) -> int:
    return execute(instructions)


def part2(instructions: list[Instruction]) -> int:
    registers = defaultdict(int)
    registers["c"] = 1

    return execute(instructions, registers)


if __name__ == "__main__":
    input = sys.stdin.read()
    instructions = parse(input)

    result1, elapsed = timed(part1, instructions)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, instructions)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
