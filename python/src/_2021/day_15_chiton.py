import heapq
import sys
from collections import defaultdict

from aoc.util import adjacent4, timed


def parse(input: str) -> list[list[int]]:
    return [[int(digit) for digit in row] for row in input.strip().splitlines()]


def min_risk_path(grid: list[list[int]], *, n_expansions: int) -> int:
    n_rows0 = len(grid)
    n_cols0 = len(grid[0])
    n_rows = n_expansions * n_rows0
    n_cols = n_expansions * n_cols0

    def risk(row: int, col: int) -> int:
        elem = grid[row % n_rows0][col % n_cols0]
        offset = (row // n_rows0) + (col // n_cols0)
        return (elem + offset - 1) % 9 + 1

    prio_queue = [(0, (0, 0))]
    best_risks = defaultdict(lambda: sys.maxsize)

    while prio_queue:
        total_risk, coord = heapq.heappop(prio_queue)

        if coord == (n_rows - 1, n_cols - 1):
            return total_risk

        for neighbor in adjacent4(coord):
            nr, nc = neighbor
            if not (nr in range(n_rows) and nc in range(n_cols)):
                continue

            neighbor_risk = total_risk + risk(nr, nc)
            if neighbor_risk < best_risks[neighbor]:
                best_risks[neighbor] = neighbor_risk
                heapq.heappush(prio_queue, (neighbor_risk, neighbor))

    raise RuntimeError("No path found to the bottom right")


def part1(grid: list[list[int]]) -> int:
    return min_risk_path(grid, n_expansions=1)


def part2(grid: list[list[int]]) -> int:
    return min_risk_path(grid, n_expansions=5)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
