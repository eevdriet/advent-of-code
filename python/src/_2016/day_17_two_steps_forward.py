import sys
from collections import deque
from hashlib import md5

from aoc.io import open_file
from aoc.util import timed


def parse(input: str) -> str:
    return input


def is_open(door: str) -> bool:
    return door[0] in "bcdef"


def find_vault(
    passcode: str,
    grid: list[str],
    start: tuple[int, int],
    goal: tuple[int, int],
    part2: bool = False,
) -> str:
    directions = ["U", "D", "L", "R"]
    queue = deque([((1, 1), "")])
    seen = set([start])
    max_len = 0

    while queue:
        coord, path = queue.popleft()
        row, col = coord

        if (row + 1, col + 1) == goal:
            if not part2:
                return path

            max_len = max(len(path), max_len)
            continue

        hash = md5(f"{passcode}{''.join(path)}".encode()).hexdigest()

        seen_options = []

        for dir, (dr, dc) in enumerate([(-1, 0), (1, 0), (0, -1), (0, 1)]):
            r = row + dr
            c = col + dc

            if not is_open(hash[dir]) or grid[r][c] == "#":
                continue

            next_coord = row + 2 * dr, col + 2 * dc
            option = (next_coord, path + directions[dir])

            if next_coord in seen:
                seen_options.append(option)
            else:
                seen.add(next_coord)
                queue.append(option)

        queue.extend(seen_options)

    return str(max_len)


def part1(passcode: str) -> str:
    with open_file(2016, 17, name="vault") as file:
        grid = file.read().strip().splitlines()

    return find_vault(passcode, grid, (1, 1), (8, 8))


def part2(passcode: str) -> str:
    with open_file(2016, 17, name="vault") as file:
        grid = file.read().strip().splitlines()

    return find_vault(passcode, grid, (1, 1), (8, 8), part2=True)


if __name__ == "__main__":
    # input = sys.stdin.read()
    # parsed = parse(input)
    #
    # result1, elapsed = timed(part1, parsed)
    # print(f"Part 1: {result1} ({elapsed} elapsed)")
    #
    # result2, elapsed = timed(part2, parsed)
    # print(f"Part 2: {result2} ({elapsed} elapsed)")

    part1("hijkl")
