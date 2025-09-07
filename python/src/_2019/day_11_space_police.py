import sys
from collections import defaultdict

from _2019.intcode import IntCode, Status
from aoc.util import timed


def parse(input: str) -> list[int]:
    return [int(num) for num in input.split(",")]


def paint_panels(memory: list[int], panels: dict[complex, int]) -> dict[complex, int]:
    robot = IntCode(memory)

    panels = defaultdict(int, panels)
    pos = 0
    dir = 1j

    while robot.status != Status.HALTED:
        inputs = [panels[pos]]
        outputs = robot.run(inputs)
        assert len(outputs) == 2

        color, int_dir = outputs
        panels[pos] = color

        dir *= 1j if int_dir == 0 else -1j
        pos += dir

    return panels


def part1(memory: list[int]) -> int:
    panels = paint_panels(memory, {})

    return len(panels)


def part2(memory: list[int]) -> str:
    panels = paint_panels(memory, {0: 1})

    x_min = min(int(coord.real) for coord in panels)
    y_min = min(int(coord.imag) for coord in panels)
    x_max = max(int(coord.real) for coord in panels)
    y_max = max(int(coord.imag) for coord in panels)

    identifier = ""

    for y in reversed(range(y_min, y_max + 1)):
        for x in range(x_min, x_max + 1):
            coord = complex(x, y)
            identifier += "#" if panels[coord] else "."

        identifier += "\n"

    return identifier.strip()


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
