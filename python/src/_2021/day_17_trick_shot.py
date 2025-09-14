import re
import sys

from attrs import define

from aoc.util import minmax, timed


@define
class Target:
    x_min: int
    x_max: int
    y_min: int
    y_max: int

    def in_bounds(self, x: int, y: int) -> bool:
        return x in range(self.x_min, self.x_max + 1) and y in range(
            self.y_min, self.y_max + 1
        )


def parse(input: str) -> Target:
    x1, x2, y1, y2 = map(int, re.findall(r"(-?\d+)", input.strip()))
    x_min, x_max = minmax(x1, x2)
    y_min, y_max = minmax(y1, y2)

    return Target(x_min, x_max, y_min, y_max)


def part1(target: Target) -> int:
    y = target.y_min

    return y * (y + 1) // 2


def part2(target: Target) -> int:
    def simulate(velo_x: int, velo_y: int, x: int, y: int) -> int:
        if x > target.x_max or y < target.y_min:
            return 0
        if x >= target.x_min and y <= target.y_max:
            return 1

        return simulate(velo_x - (velo_x > 0), velo_y - 1, x + velo_x, y + velo_y)

    return sum(
        simulate(velo_x, velo_y, 0, 0)
        for velo_x in range(1, target.x_max + 1)
        for velo_y in range(target.y_min, -target.y_min + 1)
    )


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
