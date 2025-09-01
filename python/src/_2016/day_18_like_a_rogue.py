import sys

from aoc.util import timed


def parse(input: str) -> str:
    return input.strip()


def count_safe_tiles(row: str, n_rows: int):
    count = row.count(".")
    n_cols = len(row)

    def is_trap(left: str, right: str, _center: str) -> bool:
        return left != right

    for _ in range(n_rows - 1):
        new_row = ""

        for col in range(n_cols):
            left = row[col - 1] if col - 1 >= 0 else "."
            right = row[col + 1] if col + 1 < n_cols else "."
            center = row[col] if col > 0 else "."

            new_row += "^" if is_trap(left, right, center) else "."

        row = new_row
        count += row.count(".")

    return count


def part1(start_row: str) -> int:
    return count_safe_tiles(start_row, 40)


def part2(start_row: str) -> int:
    return count_safe_tiles(start_row, 400_000)


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
