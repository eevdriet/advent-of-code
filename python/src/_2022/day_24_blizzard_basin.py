import sys
from collections import deque
from itertools import pairwise
from math import lcm

from attrs import define

from aoc.io import read_file
from aoc.util import timed

STEP_DIRECTIONS = {">": (1, 0), "<": (-1, 0), "v": (0, 1), "^": (0, -1)}

Coord = tuple[int, int]


@define
class Mountain:
    blizzards: list[tuple[Coord, str]]
    n_rows: int
    n_cols: int

    start: Coord
    end: Coord

    def _calculate_blizzard_lookup(self, period: int) -> list[set[Coord]]:
        # Precompute blizzard positions for each time modulo period
        blizzards = set()
        for (x, y), dir in self.blizzards:
            blizzards.add((x, y, dir))

        lookup = []

        for t in range(period):
            positions = {(x, y) for (x, y, _) in blizzards}
            lookup.append(positions)

            next_blizzards = set()

            for x, y, dir in blizzards:
                dx, dy = STEP_DIRECTIONS[dir]
                nx = (x + dx) % self.n_cols
                ny = (y + dy) % self.n_rows
                next_blizzards.add((nx, ny, dir))

            blizzards = next_blizzards

        return lookup

    def traverse(self, path: list[Coord]) -> int:
        period = lcm(self.n_rows, self.n_cols)
        lookup = self._calculate_blizzard_lookup(period)

        # BFS through (coord, time % period)
        def bfs(start: Coord, end: Coord, start_time: int) -> int:
            queue = deque([(start, start_time)])
            seen = set()

            while queue:
                (x, y), time = queue.popleft()

                if (x, y) == end:
                    return time

                next_time = time + 1
                blizzards = lookup[next_time % period]

                for dx, dy in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx = x + dx
                    ny = y + dy
                    neighbor = nx, ny

                    # inside map or at start/end
                    if nx not in range(self.n_cols) or ny not in range(self.n_rows):
                        if neighbor not in [self.start, self.end]:
                            continue

                    if (nx, ny) in blizzards:
                        continue

                    state = (neighbor, next_time % period)
                    if state in seen:
                        continue

                    seen.add(state)
                    queue.append((neighbor, next_time))

            raise RuntimeError("No path found")

        time = 0
        for start, end in pairwise(path):
            time = bfs(start, end, time)

        return time


def parse(input: str) -> Mountain:
    lines = input.splitlines()
    n_rows = len(lines) - 2  # without walls
    n_cols = len(lines[0]) - 2

    blizzards = []
    for y, line in enumerate(lines[1:-1]):  # skip outer walls
        for x, cell in enumerate(line[1:-1]):
            if cell in STEP_DIRECTIONS:
                blizzards.append(((x, y), cell))

    start = (lines[0].index(".") - 1, -1)  # just outside top
    end = (lines[-1].index(".") - 1, n_rows)  # just outside bottom

    return Mountain(blizzards, n_rows, n_cols, start, end)


def part1(mountain: Mountain) -> int:
    path = [mountain.start, mountain.end]
    return mountain.traverse(path)


def part2(mountain: Mountain) -> int:
    path = [mountain.start, mountain.end, mountain.start, mountain.end]
    return mountain.traverse(path)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    example = read_file(2022, 24, "example2")
    part2(parse(example))
