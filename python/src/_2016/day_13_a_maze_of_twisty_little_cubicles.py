import sys
from collections import deque
from typing import Optional

from aoc.util import adjacent4, timed


def parse(input: str) -> int:
    return int(input)


def is_wall(x: int, y: int, key: int) -> bool:
    if x < 0 or y < 0:
        return True

    num = x * x + 3 * x + 2 * x * y + y + y * y + key
    return bin(num).count("1") % 2 == 1


def find_goal(goal: tuple[int, int], key: int, max_steps: Optional[int] = None):
    start = (1, 1)
    seen = {start}
    queue = deque([(start, 0)])

    while queue:
        coord, n_steps = queue.popleft()

        if max_steps is None and coord == goal:
            return n_steps

        if max_steps is not None and n_steps >= max_steps:
            continue

        for next_coord in adjacent4(coord):
            if is_wall(next_coord[0], next_coord[1], key):
                continue
            if next_coord in seen:
                continue

            seen.add(next_coord)  # ✅ mark here
            queue.append((next_coord, n_steps + 1))

    return len(seen)


def part1(key: int) -> int:
    goal = (31, 39)

    return find_goal(goal, key)


def part2(key: int) -> int:
    goal = (31, 39)

    return find_goal(goal, key, max_steps=50)


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
