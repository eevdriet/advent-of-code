import sys

from aoc.io import open_file
from aoc.util import timed

Grid = dict[complex, str]


def parse(input: str) -> tuple[Grid, complex]:
    grid = {}
    lines = input.splitlines()
    mid = len(lines) // 2

    for r, row in enumerate(lines):
        for c, ch in enumerate(row.strip()):
            if ch == "#":
                coord = (c - mid) + (r - mid) * 1j
                grid[coord] = "#"

    return grid, 0 + 0j


def simulate_virus(
    grid: Grid, start: complex, n_iters: int, *, part2: bool = False
) -> int:
    n_infected = 0
    pos = start
    dir = -1j

    def evolve(state: str, dir: complex) -> tuple[str, complex, bool]:
        turns_infected = False

        match state:
            case ".":
                state = "W" if part2 else "#"
                turns_infected = not part2
                dir *= -1j
            case "W":
                state = "#"
                turns_infected = part2
            case "#":
                state = "F" if part2 else "."
                dir *= 1j
            case "F":
                state = "."
                dir *= -1

        return state, dir, turns_infected

    for _ in range(n_iters):
        # Determine how the node at the current position should evolve
        state = grid.get(pos, ".")
        next, dir, turns_infected = evolve(state, dir)

        # Set the next state, move on
        grid[pos] = next
        pos += dir

        # Register whether the node became infected
        n_infected += turns_infected

    return n_infected


def part1(grid: Grid, start: complex) -> int:
    return simulate_virus(grid, start, 10_000, part2=False)


def part2(grid: Grid, start: complex) -> int:
    return simulate_virus(grid, start, 10_000_000, part2=True)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, *parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    with open_file(2017, 22, name="example") as file:
        part1(*parse(file.read()))
