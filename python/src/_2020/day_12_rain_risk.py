import re
import sys

from aoc.util import timed

Instruction = tuple[str, int]


def parse(input: str) -> list[Instruction]:
    instructions = []
    for line in input.splitlines():
        match = re.match(r"([FNESWLR])(\d+)", line)
        action, n_steps = match.groups()

        instructions.append((action, int(n_steps)))

    return instructions


def part1(instructions: list[Instruction]) -> int:
    pos = 0
    dir = 1

    for action, n_steps in instructions:
        match action:
            case "N":
                pos += n_steps * 1j
            case "E":
                pos += n_steps * 1
            case "S":
                pos += n_steps * -1j
            case "W":
                pos += n_steps * -1
            case "F":
                pos += n_steps * dir
            case "L":
                dir *= 1j ** (n_steps // 90)
            case "R":
                dir /= 1j ** (n_steps // 90)
            case _:
                raise ValueError(f"Read invalid action '{action}'")

    return int(abs(pos.real) + abs(pos.imag))


def part2(instructions: list[Instruction]) -> int:
    pos = 0
    waypoint = 10 + 1j

    for action, n_steps in instructions:
        match action:
            case "N":
                waypoint += n_steps * 1j
            case "E":
                waypoint += n_steps * 1
            case "S":
                waypoint += n_steps * -1j
            case "W":
                waypoint += n_steps * -1
            case "F":
                pos += n_steps * waypoint
            case "L":
                waypoint *= 1j ** (n_steps // 90)
            case "R":
                waypoint /= 1j ** (n_steps // 90)
            case _:
                raise ValueError(f"Read invalid action '{action}'")

    return int(abs(pos.real) + abs(pos.imag))


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
