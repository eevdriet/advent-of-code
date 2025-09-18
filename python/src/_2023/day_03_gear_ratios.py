import sys
from collections import defaultdict

from aoc.io import read_file
from aoc.util import timed
from aoc.util.adjacent import adjacent8

Schematic = dict[complex, str]


def parse(text: str) -> Schematic:
    symbols = defaultdict(lambda: " ")

    for y, line in enumerate(text.splitlines()):
        for x, symbol in enumerate(line):
            if symbol == ".":
                continue

            coord = complex(x, y)
            symbols[coord] = symbol

    return symbols


def part1(schematic: Schematic) -> int:
    total = 0
    digits = {coord for coord, symbol in schematic.items() if symbol.isdigit()}

    used = set()

    def gear_adjacent(*coords: complex) -> bool:
        return any(
            not (schematic[coord].isdigit() or schematic[coord].isspace())
            for coord in coords
        )

    for coord in digits:
        if coord in used:
            continue

        num = schematic[coord]
        used.add(coord)
        is_adjacent = gear_adjacent(coord + 1j, coord - 1j)

        left = coord - 1
        while schematic[left].isdigit():
            used.add(left)
            num = f"{schematic[left]}{num}"

            is_adjacent |= gear_adjacent(left + 1j, left - 1j)
            left -= 1

        right = coord + 1
        while schematic[right].isdigit():
            used.add(right)
            num = f"{num}{schematic[right]}"

            is_adjacent |= gear_adjacent(right + 1j, right - 1j)
            right += 1

        is_adjacent |= gear_adjacent(
            left, left + 1j, left - 1j, right, right + 1j, right - 1j
        )
        if is_adjacent:
            total += int(num)

    return total


def part2(schematic: Schematic) -> int:
    total = 0
    gears = {coord for coord, symbol in schematic.items() if symbol == "*"}

    for gear in gears:
        used = set()
        nums = []

        for neighbor in adjacent8(gear):
            if not schematic.get(neighbor, ".").isdigit():
                continue
            if neighbor in used:
                continue

            used.add(neighbor)
            num = schematic[neighbor]

            left = neighbor - 1
            while schematic[left].isdigit():
                used.add(left)
                num = f"{schematic[left]}{num}"
                left -= 1

            right = neighbor + 1
            while schematic[right].isdigit():
                used.add(right)
                num = f"{num}{schematic[right]}"
                right += 1

            nums.append(num)

        if len(nums) == 2:
            total += int(nums[0]) * int(nums[1])

    return total


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    example = read_file(2023, 3, "example")
    part1(parse(example))
