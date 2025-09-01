import sys
from collections import defaultdict

import parse as ps

from aoc.util import minmax, timed

Coord = tuple[int, int]


class Instruction:
    def __init__(self, typ: str, coord1: Coord, coord2: Coord):
        self.typ = typ
        self.coord1 = coord1
        self.coord2 = coord2

    @classmethod
    def parse(cls, line: str):
        typ, x1, y1, x2, y2 = ps.parse("{} {:d},{:d} through {:d},{:d}", line)
        coord1 = (x1, y1)
        coord2 = (x2, y2)

        return cls(typ, coord1, coord2)

    def coords(self):
        x_min, x_max = minmax(self.coord1[0], self.coord2[0])
        y_min, y_max = minmax(self.coord1[1], self.coord2[1])

        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                yield x, y


def parse(input: str) -> list[Instruction]:
    return [Instruction.parse(line) for line in input.splitlines()]


def part1(instructions: list[Instruction]):
    lights = defaultdict(lambda: False)

    for instruction in instructions:
        for coord in instruction.coords():
            match instruction.typ:
                case "toggle":
                    lights[coord] = not lights[coord]
                case "turn on":
                    lights[coord] = True
                case "turn off":
                    lights[coord] = False

    return sum(is_on for is_on in lights.values())


def part2(instructions: list[Instruction]):
    lights = defaultdict(lambda: 0)

    for instruction in instructions:
        for coord in instruction.coords():
            match instruction.typ:
                case "toggle":
                    lights[coord] += 2
                case "turn on":
                    lights[coord] += 1
                case "turn off":
                    lights[coord] = max(0, lights[coord] - 1)

    return sum(brightness for brightness in lights.values())


def main():
    input = sys.stdin.read()
    instructions = parse(input)

    result1, elapsed = timed(part1, instructions)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, instructions)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
