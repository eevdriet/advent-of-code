import sys
from collections import deque
from itertools import pairwise, permutations

from aoc.io import FileType, open_file
from aoc.util import timed

Coord = tuple[int, int]


def parse(input: str) -> list[str]:
    return input.splitlines()


def find_goals(grid: list[str]) -> dict[Coord, int]:
    goals = {}

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            cell = grid[row][col]
            if not cell.isdigit():
                continue

            goals[(row, col)] = int(cell)

    return goals


def find_distances(grid: list[str], goals: dict[Coord, int]) -> list[list[int]]:
    # Find all nodes in the grid and set up their distances
    n_nodes = len(goals)

    distances = [[sys.maxsize] * n_nodes for _ in range(n_nodes)]
    for idx in range(n_nodes):
        distances[idx][idx] = 0

    def bfs(start: Coord, idx: int):
        # Keep track of how many of the goals have been visited
        n_visited = sum(1 for distance in distances[idx] if distance < sys.maxsize)

        # Keep track of places in the grid to explore
        seen = set([start])
        queue = deque([(start, 0)])

        while queue and n_visited < len(goals):
            coord, n_steps = queue.popleft()

            # Found one of the goals: keep track of visited before
            if coord in goals:
                goal = goals[coord]

                if n_steps < distances[idx][goal]:
                    n_visited += 1

                distances[idx][goal] = n_steps
                distances[goal][idx] = n_steps

            row, col = coord

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                r = row + dr
                c = col + dc
                next_coord = (r, c)

                if grid[r][c] == "#":
                    continue
                if next_coord in seen:
                    continue

                seen.add(next_coord)
                queue.append((next_coord, n_steps + 1))

    # Search for all other nodes
    for goal, idx in goals.items():
        bfs(goal, idx)

    return distances


def part1(grid: list[str]) -> int:
    goals = find_goals(grid)
    distances = find_distances(grid, goals)

    indices = range(1, len(distances))
    min_dist = sys.maxsize

    for perm in permutations(indices):
        dist_mid = sum(distances[src][dst] for src, dst in pairwise(perm))
        dist_start = distances[0][perm[0]]

        min_dist = min(dist_start + dist_mid, min_dist)

    return min_dist


def part2(grid: list[str]) -> int:
    goals = find_goals(grid)
    distances = find_distances(grid, goals)

    indices = range(1, len(distances))
    min_dist = sys.maxsize

    for perm in permutations(indices):
        dist_mid = sum(distances[src][dst] for src, dst in pairwise(perm))
        dist_start = distances[0][perm[0]]
        dist_end = distances[perm[-1]][0]

        min_dist = min(dist_start + dist_mid + dist_end, min_dist)

    return min_dist


if __name__ == "__main__":
    # input = sys.stdin.read()
    # parsed = parse(input)
    #
    # result1, elapsed = timed(part1, parsed)
    # print(f"Part 1: {result1} ({elapsed} elapsed)")
    #
    # result2, elapsed = timed(part2, parsed)
    # print(f"Part 2: {result2} ({elapsed} elapsed)")

    with open_file(2016, 24, FileType.EXAMPLE) as file:
        grid = parse(file.read())

    part1(grid)
