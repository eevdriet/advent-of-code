import sys

from aoc.util import timed


def parse(input: str) -> list[str]:
    return input.splitlines()


def part1(directions: list[str]) -> str:
    row = 1
    col = 1
    digits = []

    for line in directions:
        for dir in line:
            match dir:
                case "U":
                    row = max(0, row - 1)
                case "R":
                    col = min(2, col + 1)
                case "D":
                    row = min(2, row + 1)
                case "L":
                    col = max(0, col - 1)

        digit = str(1 + 3 * row + col)
        digits.append(digit)

    return "".join(digits)


def part2(directions: list[str]) -> str:
    row, col = 0, -2
    digits = []

    def symbol_at(row: int, col: int) -> str:
        # Starting value at the leftmost cell of each row (in reading order)
        # start_idx is 0-based count of symbols before this row.
        start_idx = (row + 2) ** 2 if row <= 0 else 9 + (row - 1) * 3

        # Move within the row by how far 'col' is from the leftmost col: -(2 - |row|)
        val = 1 + start_idx + col + (2 - abs(row))  # 1..13 (10=A, 11=B, 12=C, 13=D)

        return str(val) if val <= 9 else chr(ord("A") + val - 10)

    for line in directions:
        for dir in line:
            match dir:
                case "U" if abs(row - 1) + abs(col) <= 2:
                    row -= 1
                case "R" if abs(row) + abs(col + 1) <= 2:
                    col += 1
                case "D" if abs(row + 1) + abs(col) <= 2:
                    row += 1
                case "L" if abs(row) + abs(col - 1) <= 2:
                    col -= 1

        digits.append(symbol_at(row, col))

    return "".join(digits)


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
