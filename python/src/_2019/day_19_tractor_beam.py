import sys

from attrs import define

from _2019.intcode import IntCode
from aoc.util import timed

Coord = tuple[int, int]


@define
class Beam:
    memory: list[int]

    def is_included(self, x: int, y: int) -> bool:
        program = IntCode(self.memory.copy())
        output = program.run([x, y])

        return output[-1] == 1

    def find_coords(self, x_max: int, y_max: int) -> set[Coord]:
        coords = set()

        for x in range(x_max):
            for y in range(y_max):
                if self.is_included(x, y):
                    coords.add((x, y))

        return coords

    def find_edges(self, y_max: int) -> tuple[list[int], list[int]]:
        lefts = []
        rights = []

        x_left = 0
        x_right = 0

        for y in range(y_max):
            # Find left edge: first x with beam
            while not self.is_included(x_left, y):
                x_left += 1
            lefts.append(x_left)

            # Find right edge: last x with beam
            x_right = max(x_left, x_right)

            while self.is_included(x_right, y):
                x_right += 1

            rights.append(x_right - 1)

        return lefts, rights

    def find_square(self, size: int, y_max: int) -> Coord:
        lefts, rights = self.find_edges(y_max)

        for y in range(y_max - size):
            x = rights[y] - size + 1

            if lefts[y + size - 1] <= x:
                return x, y

        raise RuntimeError(f"Couldn't find square of size {size} for y_max {y_max}")


def parse(input: str) -> list[int]:
    return [int(num) for num in input.strip().split(",")]


def part1(memory: list[int]) -> int:
    beam = Beam(memory)
    coords = beam.find_coords(50, 50)

    return len(coords)


def part2(memory: list[int]) -> int:
    beam = Beam(memory)
    x, y = beam.find_square(100, 2000)

    return 10_000 * x + y


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
