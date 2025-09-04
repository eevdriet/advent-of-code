import heapq
import sys
from itertools import product

import parse as ps
from attrs import Factory, define, field

from aoc.util import timed


@define
class Bot:
    id: int

    x: int
    y: int
    z: int
    radius: int

    coords: list[int] = field(
        default=Factory(lambda self: [self.x, self.y, self.y], takes_self=True)
    )

    @classmethod
    def parse(cls, id: int, line: str) -> "Bot":
        x, y, z, r = ps.parse("pos=<{:d},{:d},{:d}>, r={:d}", line)
        return cls(id, x, y, z, r)

    def dist(self, other: "Bot") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def intersects(self, other: "Bot") -> int:
        return self.dist(other) <= self.radius + other.radius


def parse(input: str) -> list[Bot]:
    return [Bot.parse(id, line) for id, line in enumerate(input.splitlines())]


def part1(bots: list[Bot]) -> int:
    max_range_bot = max(bots, key=lambda bot: bot.radius)

    return sum(1 for bot in bots if bot.dist(max_range_bot) <= max_range_bot.radius)


def part2(bots: list[Bot]) -> int:
    # Find the bounds of all bots together
    coords = [[bot.coords[dimension] for bot in bots] for dimension in range(3)]
    x_min, y_min, z_min = [min(axis) for axis in coords]
    x_max, y_max, z_max = [max(axis) for axis in coords]

    # Start searching with a cube that covers the full bounds, where the side length = 2^n
    size = 1
    while size < max(x_max - x_min, y_max - y_min, z_max - z_min):
        size *= 2

    # Keep track of regions where the intersection count is maximal
    queue = [(0, size, x_min, y_min, z_min)]

    while queue:
        _, size, x, y, z = heapq.heappop(queue)

        if size == 1:
            return abs(x) + abs(y) + abs(z)

        half = size // 2

        # Create a sub-cube from half the size
        for dx, dy, dz in product([0, half], repeat=3):
            nx = x + dx
            ny = y + dy
            nz = z + dz

            # Count how many bots intersect within the sub-cube
            count = 0

            for bot in bots:
                max_dist = (
                    max(0, nx - bot.x, bot.x - (nx + half - 1))
                    + max(0, ny - bot.y, bot.y - (ny + half - 1))
                    + max(0, nz - bot.z, bot.z - (nz + half - 1))
                )
                if max_dist <= bot.radius:
                    count += 1

            heapq.heappush(queue, (-count, half, nx, ny, nz))

    raise RuntimeError("No solutions found")


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
