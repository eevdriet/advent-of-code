import heapq
import sys
from enum import Enum, IntEnum, auto

import parse as ps

from aoc.io import read_file
from aoc.util import adjacent4, timed


class Region(IntEnum):
    ROCKY = 0  # "."
    WET = 1  # "="
    NARROW = 2  # "|"


class Gear(IntEnum):
    NONE = 0
    TORCH = 1
    CLIMBING = 2


MOD = 20_183

Coord2D = tuple[int, int]


def parse(input: str) -> tuple[int, Coord2D]:
    depth, x_max, y_max = ps.parse("depth: {:d}\ntarget: {:d},{:d}", input.strip())
    target = x_max, y_max

    return depth, target


def create_indices(depth: int, target: Coord2D) -> dict[Coord2D, tuple[int, Region]]:
    geo_indices: dict[Coord2D, tuple[int, Region]] = {}
    x_max, y_max = target

    for y in range(y_max + 1):
        for x in range(x_max + 1):
            match (x, y):
                case coord if coord in [(0, 0), target]:
                    geo = 0
                case (x, 0):
                    geo = x * 16_807
                case (0, y):
                    geo = y * 48_271
                case _:
                    ero_x, _ = geo_indices[(x - 1, y)]
                    ero_y, _ = geo_indices[(x, y - 1)]

                    geo = ero_x * ero_y

            ero = (geo + depth) % MOD
            risk = Region(ero % 3)

            geo_indices[(x, y)] = ero, risk

    return geo_indices


def part1(depth: int, target: Coord2D) -> int:
    geo_indices = create_indices(depth, target)

    return sum(risk for _, risk in geo_indices.values())


def part2(depth: int, target: Coord2D) -> int:
    # Create a larger grid based on the target
    x_max, y_max = target
    x_max += 1000
    y_max += 1000
    geo_indices = create_indices(depth, (x_max, y_max))

    def is_compatible(gear: Gear, region: Region):
        REGION_GEAR_OPTIONS = {
            Region.ROCKY: [Gear.CLIMBING, Gear.TORCH],
            Region.WET: [Gear.CLIMBING, Gear.NONE],
            Region.NARROW: [Gear.TORCH, Gear.NONE],
        }

        return gear in REGION_GEAR_OPTIONS[region]

    prio_queue = [(0, (0, 0, Gear.TORCH))]
    seen = {}

    while prio_queue:
        n_minutes, key = heapq.heappop(prio_queue)
        x, y, gear = key

        # Better answer seen before: continue
        if key in seen and n_minutes >= seen[key]:
            continue

        seen[key] = n_minutes

        # Target reached with the right tool: done
        if (x, y) == target and gear == Gear.TORCH:
            return n_minutes

        _, region = geo_indices[(x, y)]

        # Stay in place and switch to proper gear
        for other_gear in Gear:
            if gear != other_gear and is_compatible(other_gear, region):
                next_state = (n_minutes + 7, (x, y, other_gear))
                heapq.heappush(prio_queue, next_state)

        # Move to neighbors
        for nx, ny in adjacent4((x, y)):
            if (nx, ny) not in geo_indices:
                continue

            _, nregion = geo_indices[(nx, ny)]
            if is_compatible(gear, nregion):
                next_state = (n_minutes + 1, (nx, ny, gear))
                heapq.heappush(prio_queue, next_state)

    raise RuntimeError("No path found")


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, *parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2018, 22)
    depth = 510
    target = 10, 10

    print(part1(*parse(f"depth: {depth}\ntarget: {target[0]},{target[1]}")))
