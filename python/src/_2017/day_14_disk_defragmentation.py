import sys

from _2017.day_10_knot_hash import part2 as knot_hash
from aoc.io import open_file
from aoc.util import timed


def parse(input: str) -> str:
    return input.strip()


def hex_to_bin(num_str: str) -> str:
    return "".join(f"{int(digit, 16):04b}" for digit in num_str)


def part1(key_str: str) -> int:
    n_squares = 0

    for round in range(128):
        # Create the bits for every single round
        hash = knot_hash(f"{key_str}-{round}")
        bits = hex_to_bin(hash)

        # Determine how many bits are used
        n_squares += bits.count("1")

    return n_squares


def part2(key_str: str) -> int:
    used = set()

    for row in range(128):
        hash = knot_hash(f"{key_str}-{row}")
        bits = hex_to_bin(hash)

        # Now remember where the used bits are
        for col, bit in enumerate(bits):
            if bit == "1":
                used.add((row, col))

    # Then use flood-fill to find how many regions there are
    visited = set()

    def flood(row: int, col: int):
        coord = row, col

        # Coordinate out of bounds
        if not (row in range(128) and col in range(128)):
            return 0

        # Coordinate not in use: cannot extend group
        if coord not in used:
            return 0

        # Coordinate already used in group: do not continue
        if coord in visited:
            return 0

        visited.add(coord)

        # Try to go to all neighbors
        return (
            1
            + flood(row + 1, col)
            + flood(row - 1, col)
            + flood(row, col + 1)
            + flood(row, col - 1)
        )

    # Every group is started from some coordinate
    return sum(1 for coord in used if flood(*coord) > 0)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    part2("flqrgnkx")
