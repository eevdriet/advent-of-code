import sys
from typing import Literal

from attrs import define

from aoc.io import read_file
from aoc.util import timed

Instruction = Literal["L"] | Literal["R"] | int


@define
class MonkeyMap:
    tiles: dict[complex, str]
    start: complex

    @classmethod
    def parse(cls, text: str) -> "MonkeyMap":
        tiles = {}
        start = -1j

        for y, line in enumerate(text.splitlines()):
            for x, tile in enumerate(line):
                coord = complex(x, y)

                if tile == " ":
                    continue

                if start.imag < 0:
                    start = coord

                tiles[coord] = tile

        return cls(tiles, start)

    @property
    def n_rows(self):
        return max(int(coord.imag) for coord in self.tiles) + 1

    @property
    def n_cols(self):
        return max(int(coord.real) for coord in self.tiles) + 1

    def find_next(self, coord: complex, dir: complex) -> complex:
        # Determine the next coordinate and return right away if it exists
        ncoord = coord + dir

        if ncoord in self.tiles:
            return ncoord

        # Otherwise, find the first coordinate on the other side of the map
        col = int(coord.real)
        row = int(coord.imag)

        match dir:
            # Right
            case 1:
                return next(
                    complex(c, row)
                    for c in range(self.n_cols)
                    if complex(c, row) in self.tiles
                )
            # Left
            case -1:
                return next(
                    complex(c, row)
                    for c in reversed(range(self.n_cols))
                    if complex(c, row) in self.tiles
                )
            # Down
            case 1j:
                return next(
                    complex(col, r)
                    for r in range(self.n_rows)
                    if complex(col, r) in self.tiles
                )
            # Up
            case -1j:
                return next(
                    complex(col, r)
                    for r in reversed(range(self.n_rows))
                    if complex(col, r) in self.tiles
                )
            case _:
                raise ValueError(f"Found invalid direction '{dir}'")


def parse(input: str) -> tuple[MonkeyMap, list[Instruction]]:
    map_text, instruction_text = input.split("\n\n")
    map = MonkeyMap.parse(map_text)

    instructions = []
    num = ""

    for ch in instruction_text.strip():
        match ch:
            case ch if ch.isdigit():
                num += ch
            case ch if ch in ["L", "R"]:
                if num:
                    instructions.append(int(num))
                    num = ""

                instructions.append(ch)
            case _:
                raise ValueError(f"Found invalid character '{ch}' in instruction text")
    if num:
        instructions.append(int(num))

    return map, instructions


def part1(map: MonkeyMap, instructions: list[Instruction]) -> int:
    coord = map.start
    dir = 1

    for instruction in instructions:
        match instruction:
            case "L":
                dir *= -1j
            case "R":
                dir *= 1j
            case n_steps:
                for _ in range(n_steps):
                    ncoord = map.find_next(coord, dir)
                    if map.tiles[ncoord] == "#":
                        break

                    coord = ncoord

    # Compute the password
    row = int(coord.imag) + 1
    col = int(coord.real) + 1
    dir_num = {1: 0, 1j: 1, -1: 2, -1j: 3}

    return 1000 * row + 4 * col + dir_num[dir]


def part2(map: MonkeyMap, instructions: list[Instruction]) -> int:
    return 0


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, *parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    example = read_file(2022, 22, "example")
    part1(*parse(example))
