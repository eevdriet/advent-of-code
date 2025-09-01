import sys

from aoc.util import timed

Direction = tuple[str, int]


def parse(input: str) -> list[Direction]:
    return [(line[0], int(line[1:])) for line in input.split(", ")]


def find_head_quarters(directions: list[Direction], stop_at_visited: bool) -> int:
    # Start at the zero position facing north
    dir = 0
    pos = 0 + 0j
    dirs = [0 + 1j, 1 + 0j, 0 - 1j, -1 + 0j]

    # Keep track of previously visited positions
    seen = {pos}
    seen_before = False

    for side, width in directions:
        dir = dir + 1 if side == "L" else dir - 1
        dir = dir % 4

        for _ in range(width):
            pos += dirs[dir]

            if stop_at_visited and pos in seen:
                seen_before = True
                break

            seen.add(pos)

        if seen_before:
            break

    return int(abs(pos.imag) + abs(pos.real))


def part1(directions: list[Direction]) -> int:
    return find_head_quarters(directions, stop_at_visited=False)


def part2(directions: list[Direction]) -> int:
    return find_head_quarters(directions, stop_at_visited=True)


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
