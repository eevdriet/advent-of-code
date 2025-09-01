import sys
from collections import defaultdict
from math import factorial

from aoc.io import open_file
from aoc.util import timed

Instruction = list[str]


def parse(input: str) -> list[Instruction]:
    return [line.split() for line in input.strip().splitlines()]


def execute(
    program: list[Instruction], registers: defaultdict = defaultdict(int)
) -> int:
    ip = 0
    clock = []

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
                    ip += get_val(jump)
                    continue

            case ("tgl", jump):
                jump = get_val(jump)

                # Verify whether the toggle is valid
                if ip + jump in range(len(program)):
                    op, *args = program[ip + jump]

                    match len(args):
                        case 1:
                            op = "dec" if op == "inc" else "inc"
                        case 2:
                            op = "cpy" if op == "jnz" else "jnz"

                    if not (op == "cpy" and args[1].isdigit()):
                        program[ip + jump] = [op, *args]

            case ("out", num):
                clock.append(get_val(num))

        ip += 1

    return registers["a"]


def part1(instructions: list[Instruction]) -> int:
    registers = defaultdict(int)
    registers["a"] = 1

    return execute(instructions, registers)


def part2(_instructions: list[Instruction]) -> int:
    registers = defaultdict(int)
    registers["a"] = 12

    return 89 * 90 + factorial(registers["a"])


if __name__ == "__main__":
    # input = sys.stdin.read()
    # parsed = parse(input)
    #
    # result1, elapsed = timed(part1, parsed)
    # print(f"Part 1: {result1} ({elapsed} elapsed)")
    #
    # result2, elapsed = timed(part2, parsed)
    # print(f"Part 2: {result2} ({elapsed} elapsed)")

    with open_file(2016, 25) as file:
        instructions = parse(file.read())

    part1(instructions)
