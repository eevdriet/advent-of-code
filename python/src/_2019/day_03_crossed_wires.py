import sys

from aoc.util import timed

Direction = tuple[str, int]
Wire = list[Direction]

STEPS = {"U": 1j, "R": 1, "D": -1j, "L": -1}


def parse(input: str) -> tuple[Wire, Wire]:
    line1, line2 = input.splitlines()

    def parse_wire(line: str) -> Wire:
        return [(dir[0], int(dir[1:])) for dir in line.split(",")]

    return parse_wire(line1), parse_wire(line2)


def cross(wire1: Wire, wire2: Wire, *, objective: str) -> int:
    seen = {}  # Keep track of seen positions and after how many steps
    total_steps = 0
    pos = 0

    # Register all positions the first wire occupies
    for dir, n_steps in wire1:
        step = STEPS[dir]

        for _ in range(1, n_steps + 1):
            total_steps += 1
            pos += step
            seen[pos] = total_steps

    # Do the same for the second, but keep tracck of intersections
    min_dist = sys.maxsize
    total_steps = 0
    pos = 0

    for dir, n_steps in wire2:
        step = STEPS[dir]

        for _ in range(1, n_steps + 1):
            total_steps += 1
            pos += step

            if pos in seen:
                match objective:
                    case "manhattan":
                        dist = abs(pos.real) + abs(pos.imag)
                    case _:
                        dist = seen[pos] + total_steps

                min_dist = min(dist, min_dist)

    return int(min_dist)


def part1(wire1: Wire, wire2: Wire) -> int:
    return cross(wire1, wire2, objective="manhattan")


def part2(wire1: Wire, wire2: Wire) -> int:
    return cross(wire1, wire2, objective="steps")


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, *parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
