import sys
from collections import deque
from copy import deepcopy

from _2019.intcode import IntCode
from aoc.constant import MISSING_INT
from aoc.util import timed

Coord = tuple[int, int]


def parse(input: str) -> list[int]:
    return [int(num) for num in input.split(",")]


def explore_regions(
    memory: list[int], *, stop_when_oxygen_found: bool
) -> tuple[dict[Coord, str], int]:
    regions: dict[Coord, str] = {(0, 0): "."}
    queue = deque([(0, (IntCode(memory), 0, 0))])
    dist_to_oxygen = MISSING_INT

    while queue:
        dist, (program, x, y) = queue.popleft()

        for dir in range(1, 5):
            # Retrieve output to see whether a wall or the oxygen system is found
            dir_program = deepcopy(program)
            outputs = dir_program.run([dir])
            assert len(outputs) == 1

            # Otherwise, update the position and explore further
            nx, ny = x, y

            match dir:
                case 1:
                    ny -= 1
                case 2:
                    ny += 1
                case 3:
                    nx -= 1
                case 4:
                    nx += 1
                case _:
                    raise ValueError(
                        f"Direction {dir} should have been N/S/W/E (1 to 4)"
                    )

            if outputs[-1] == 0:
                regions[(nx, ny)] = "#"
                continue
            if outputs[-1] == 2:
                regions[(nx, ny)] = "O"
                dist_to_oxygen = dist + 1

                if stop_when_oxygen_found:
                    return regions, dist_to_oxygen
                else:
                    continue

            if (nx, ny) in regions:
                continue

            regions[(nx, ny)] = "."
            queue.append((dist + 1, (dir_program, nx, ny)))

    return regions, dist_to_oxygen


def part1(memory: list[int]) -> int:
    _, dist_to_oxygen = explore_regions(memory, stop_when_oxygen_found=True)
    return dist_to_oxygen


def part2(memory: list[int]) -> int:
    regions, _ = explore_regions(memory, stop_when_oxygen_found=False)

    oxygen = next((coord for coord in regions if regions[coord] == "O"), None)
    if not oxygen:
        raise ValueError("Regions should include oxygen system")

    queue = deque([(oxygen)])
    seen = {oxygen}
    n_minutes = -1

    while queue:
        n_minutes += 1

        for _ in range(len(queue)):
            x, y = queue.popleft()

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx = x + dx
                ny = y + dy

                if (nx, ny) in seen:
                    continue
                if regions[(nx, ny)] == "#":
                    continue

                seen.add((nx, ny))
                queue.append((nx, ny))

    return n_minutes


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
