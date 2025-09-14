import sys
from collections.abc import Generator
from typing import Callable

from aoc.io import read_file
from aoc.util import adjacent8, directions8, timed

Seat = tuple[int, int]


def parse(input: str) -> dict[Seat, bool]:
    return {
        (row, col): False
        for row, line in enumerate(input.splitlines())
        for col, seat in enumerate(line)
        if seat == "L"
    }


def find_occupied_seats(
    seats: dict[Seat, bool],
    neighbors: Callable[[Seat], Generator[Seat, None, None]],
    limit: int,
) -> int:
    while True:
        new_seats = {}

        for seat, is_occupied in seats.items():
            occupied_neighbors = (seats[neighbor] for neighbor in neighbors(seat))

            if is_occupied:
                new_seats[seat] = sum(occupied_neighbors) < limit
            else:
                new_seats[seat] = not any(occupied_neighbors)

        if seats == new_seats:
            return sum(seats.values())

        seats = new_seats


def part1(seats: dict[Seat, bool]) -> int:
    def neighbors(seat: Seat) -> Generator[Seat, None, None]:
        for neighbor in adjacent8(seat):
            if neighbor in seats:
                yield neighbor

    return find_occupied_seats(seats, neighbors, limit=4)


def part2(seats: dict[Seat, bool]) -> int:
    n_rows = max(row for row, _ in seats) + 1
    n_cols = max(col for _, col in seats) + 1

    def neighbors(seat: Seat) -> Generator[Seat, None, None]:
        row, col = seat

        for dr, dc in directions8(seat):
            r = row + dr
            c = col + dc

            while r in range(n_rows) and c in range(n_cols):
                if (r, c) in seats:
                    yield (r, c)
                    break

                r += dr
                c += dc

    return find_occupied_seats(seats, neighbors, limit=5)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2020, 11)
    part1(parse(input))
