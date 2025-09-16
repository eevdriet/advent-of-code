import sys
from itertools import accumulate

from aoc.util import timed


def parse(input: str) -> list[int]:
    vals = []

    for line in input.splitlines():
        match line.split():
            case "noop", *_:
                vals += [0]
            case "addx", val:
                vals += [0, int(val)]
            case _:
                raise ValueError(f"Could not parse instruction '{line}'")

    return vals


def execute(program: list[int]) -> tuple[int, str]:
    total_strength = 0
    image = ""

    vals = list(accumulate([1] + program))

    for cycle, val in enumerate(vals, start=1):
        strength = cycle * val

        if cycle % 40 == 20:
            total_strength += strength

        image += "#" if (cycle - 1) % 40 - val in [-1, 0, 1] else "."

    return total_strength, image


def part1(program: list[int]) -> int:
    strength, _ = execute(program)
    return strength


def part2(program: list[int]) -> str:
    _, image = execute(program)
    return "\n".join(image[idx : idx + 40] for idx in range(0, len(image) - 1, 40))


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
