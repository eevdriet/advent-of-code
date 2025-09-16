import sys
from collections import deque

from attrs import define

from aoc.io import read_file
from aoc.util import adjacent4, timed


@define
class Hills:
    heights: dict[complex, int]
    start: complex
    end: complex


def parse(input: str) -> Hills:
    heights = {}
    start: complex
    end: complex

    for y, row in enumerate(input.splitlines()):
        for x, square in enumerate(row):
            coord = complex(x, y)

            if square == "S":
                start = coord
                height = 0
            elif square == "E":
                end = coord
                height = 25
            else:
                height = ord(square) - ord("a")

            heights[coord] = height

    return Hills(heights, start, end)


def find_route(hills: Hills, starts: list[complex]) -> int:
    queue = deque([(start, 0) for start in starts])
    seen = {start for start in starts}

    while queue:
        for _ in range(len(queue)):
            coord, n_steps = queue.popleft()
            if coord == hills.end:
                return n_steps

            for neighbor in adjacent4(coord):
                if neighbor in seen:
                    continue
                if neighbor not in hills.heights:
                    continue

                if hills.heights[neighbor] <= hills.heights[coord] + 1:
                    seen.add(neighbor)
                    queue.append((neighbor, n_steps + 1))

    raise RuntimeError(f"Couldn't reach the end {hills.end} from start {hills.start}")


def part1(hills: Hills) -> int:
    starts = [hills.start]
    return find_route(hills, starts)


def part2(hills: Hills) -> int:
    starts = [coord for coord, height in hills.heights.items() if height == 0]
    return find_route(hills, starts)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    example = read_file(2022, 12, "example")
    part1(parse(example))
