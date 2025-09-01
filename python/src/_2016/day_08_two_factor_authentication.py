import re
import sys

from aoc.util import timed

Instruction = tuple[str, int, int]


def parse(input: str) -> list[Instruction]:
    instructions = []

    for line in input.splitlines():
        match = re.match(r"(rect) (\d+)x(\d+)", line) or re.match(
            r"rotate (column|row) [xy]=(\d+) by (\d+)", line
        )
        if match:
            typ, num1, num2 = match.groups()
            instructions.append((typ, int(num1), int(num2)))

    return instructions


def apply_instructions(
    instructions: list[Instruction], n_rows: int, n_cols: int
) -> set[tuple[int, int]]:
    pixels = set()

    for instruction in instructions:
        new_pixels = set(pixels)

        match instruction:
            # Turn on rectangle in the top right
            case ("rect", y, x):
                for row in range(x):
                    for col in range(y):
                        new_pixels.add((row, col))

            case ("column", col, shift):
                row_pixels = {(row, c) for (row, c) in new_pixels if c == col}
                new_pixels -= row_pixels

                for row, col in row_pixels:
                    new_pixels.add(((row + shift) % n_rows, col))

            case ("row", row, shift):
                col_pixels = {(r, col) for (r, col) in new_pixels if r == row}
                new_pixels -= col_pixels

                for row, col in col_pixels:
                    new_pixels.add((row, (col + shift) % n_cols))

        pixels = new_pixels

    return pixels


def part1(instructions: list[Instruction], n_rows: int = 6, n_cols: int = 50) -> int:
    pixels = apply_instructions(instructions, n_rows, n_cols)
    return len(pixels)


def part2(instructions: list[Instruction], n_rows: int = 6, n_cols: int = 50) -> str:
    pixels = apply_instructions(instructions, n_rows, n_cols)
    result = "\n".join(
        "".join("#" if (row, col) in pixels else "." for col in range(n_cols))
        for row in range(n_rows)
    )

    print(result)
    return result


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
