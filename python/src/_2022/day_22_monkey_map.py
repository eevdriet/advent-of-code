import sys
from math import gcd
from typing import Callable, Literal

from attrs import define

from aoc.io import read_file
from aoc.util import timed

Instruction = Literal["L"] | Literal["R"] | int


@define
class MonkeyMap:
    tiles: dict[complex, str]
    n_rows: int
    n_cols: int

    @classmethod
    def parse(cls, text: str) -> "MonkeyMap":
        tiles = {
            (x + y * 1j): tile
            for y, line in enumerate(text.splitlines())
            for x, tile in enumerate(line)
            if tile in [".", "#"]
        }
        n_rows = max(int(coord.imag) for coord in tiles) + 1
        n_cols = max(int(coord.real) for coord in tiles) + 1

        return cls(tiles, n_rows, n_cols)

    def wrap2d(self, coord: complex, dir: complex) -> tuple[complex, complex]:
        # Otherwise, find the first coordinate on the other side of the map
        x = int(coord.real)
        y = int(coord.imag)

        match dir:
            case 1:
                return complex((x + 1) % self.n_cols, y), dir
            case -1:
                return complex((x - 1) % self.n_cols, y), dir
            case 1j:
                return complex(x, (y + 1) % self.n_rows), dir
            case -1j:
                return complex(x, (y - 1) % self.n_rows), dir

            case _:
                raise ValueError(f"Found invalid wrapping direction '{dir}'")

    def wrap3d(self, coord: complex, dir: complex) -> tuple[complex, complex]:
        x = int(coord.real)
        y = int(coord.imag)
        face_size = gcd(self.n_cols, self.n_rows)

        face_x = x // face_size
        face_y = y // face_size

        match dir, x // 50, y // 50:
            case 1j, 0, _:
                return complex(149 - x, 99), -1j
            case 1j, 1, _:
                return complex(49, x + 50), -1
            case 1j, 2, _:
                return complex(149 - x, 149), -1j
            case 1j, 3, _:
                return complex(149, x - 100), -1
            case -1j, 0, _:
                return complex(149 - x, 0), 1j
            case -1j, 1, _:
                return complex(100, x - 50), 1
            case -1j, 2, _:
                return complex(149 - x, 50), 1j
            case -1j, 3, _:
                return complex(0, x - 100), 1
            case 1, _, 0:
                return complex(0, y + 100), 1
            case 1, _, 1:
                return complex(100 + y, 49), -1j
            case 1, _, 2:
                return complex(-50 + y, 99), -1j
            case -1, _, 0:
                return complex(50 + y, 50), 1j
            case -1, _, 1:
                return complex(100 + y, 0), 1j
            case -1, _, 2:
                return complex(199, y - 100), -1

            case _:
                raise ValueError(f"Found invalid wrapping key {(dir, face_x, face_y)}")


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


def follow_instructions(
    map: MonkeyMap, instructions: list[Instruction], wrap: Callable
) -> int:
    with open("out.txt", "w") as file:
        coord = min(
            (
                coord
                for coord, tile in map.tiles.items()
                if coord.imag == 0 and tile == "."
            ),
            key=lambda tile: tile.real,
        )
        dir = 1

        for instruction in instructions:
            match instruction:
                case "L":
                    dir *= -1j
                case "R":
                    dir *= 1j

                case n_steps:
                    for _ in range(n_steps):
                        ncoord, ndir = coord + dir, dir

                        if ncoord not in map.tiles:
                            ncoord, ndir = wrap(map, ncoord, ndir)

                        if map.tiles[ncoord] == ".":
                            coord, dir = ncoord, ndir

        # Compute the password
        row = int(coord.imag) + 1
        col = int(coord.real) + 1
        dir_num = {1: 0, 1j: 1, -1: 2, -1j: 3}

        return 1000 * row + 4 * col + dir_num[dir]


def part1(map: MonkeyMap, instructions: list[Instruction]) -> int:
    return follow_instructions(map, instructions, MonkeyMap.wrap2d)


def part2(map: MonkeyMap, instructions: list[Instruction]) -> int:
    return follow_instructions(map, instructions, MonkeyMap.wrap3d)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, *parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    example = read_file(2022, 22)
    part2(*parse(example))
