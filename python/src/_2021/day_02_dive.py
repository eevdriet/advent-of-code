import sys

from aoc.util import timed

Instruction = tuple[str, int]


def parse(input: str) -> list[Instruction]:
    instructions = []

    for line in input.splitlines():
        direction, n_steps = line.split()

        instruction = direction, int(n_steps)
        instructions.append(instruction)

    return instructions


def part1(instructions: list[Instruction]) -> int:
    width = 0
    depth = 0

    for direction, n_steps in instructions:
        match direction:
            case "forward":
                width += n_steps
            case "down":
                depth += n_steps
            case "up":
                depth -= n_steps
            case _:
                raise ValueError(f"Found invalid direction '{direction}'")

    return depth * width


def part2(instructions: list[Instruction]) -> int:
    width = 0
    depth = 0
    aim = 0

    for direction, n_steps in instructions:
        match direction:
            case "forward":
                width += n_steps
                depth += aim * n_steps
            case "down":
                aim += n_steps
            case "up":
                aim -= n_steps
            case _:
                raise ValueError(f"Found invalid direction '{direction}'")

    return depth * width


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
