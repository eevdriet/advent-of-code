import sys
from typing import Callable, Generator

from aoc.io import read_file
from aoc.util import adjacent4, directions4, timed

Coord = tuple[int, int]
Bug = tuple[int, ...]


def parse(input: str) -> dict[Coord, str]:
    return {
        (x, y): cell
        for y, row in enumerate(input.splitlines())
        for x, cell in enumerate(row)
    }


def simulate_bugs(
    bugs: set[Bug],
    neighbors: Callable[[Bug], Generator[Bug]],
    *,
    part: int,
    n_minutes: int = -1,
) -> set[Bug]:
    n_simulations = 0
    seen = set()

    while True:
        key = tuple(sorted(bugs))
        if part == 1 and key in seen:
            break

        seen.add(key)

        if part == 2 and n_simulations == n_minutes:
            break

        # Consider only bugs and their neighbors for the next generation
        candidates = set()
        for bug in bugs:
            candidates |= {bug}
            candidates |= {neighbor for neighbor in neighbors(bug)}

        new_bugs = set()

        for bug in candidates:
            n_bug_neighbors = sum(1 for neighbor in neighbors(bug) if neighbor in bugs)

            # Bug survives if n == 1 bugs around it
            if bug in bugs and n_bug_neighbors == 1:
                new_bugs.add(bug)

            # Empty becomes bug if n in [1, 2] bugs around it
            if bug not in bugs and n_bug_neighbors in [1, 2]:
                new_bugs.add(bug)

        bugs = new_bugs
        n_simulations += 1

    return bugs


def part1(area: dict[Coord, str]) -> int:
    bugs = {(x, y) for (x, y), cell in area.items() if cell == "#"}
    size = max(x for x, _ in area) + 1

    def neighbors(bug: Bug) -> Generator[Coord]:
        for nx, ny in adjacent4(bug):
            if nx in range(size) and ny in range(size):
                yield nx, ny

    bugs = simulate_bugs(bugs, neighbors, part=1)
    return sum(2 ** (y * size + x) for (x, y) in bugs)


def part2(area: dict[Coord, str], n_minutes: int = 200) -> int:
    bugs = {(0, x, y) for (x, y), cell in area.items() if cell == "#"}

    size = max(x for x, _ in area) + 1
    assert size & 1
    mid = size // 2

    def neighbors(bug: Bug) -> Generator[Bug, None, None]:
        level, x, y = bug

        for dx, dy in directions4(bug):
            nx = x + dx
            ny = y + dy

            if nx in range(size) and ny in range(size) and (nx, ny) != (mid, mid):
                yield level, nx, ny

            # level + 1: outside edges
            elif nx < 0:
                yield level + 1, mid - 1, mid
            elif nx >= size:
                yield level + 1, mid + 1, mid
            elif ny < 0:
                yield level + 1, mid, mid - 1
            elif ny >= size:
                yield level + 1, mid, mid + 1

            # level - 1:
            elif (nx, ny) == (mid, mid):
                for pos in range(size):
                    if dx == -1:
                        yield level - 1, size - 1, pos
                    elif dx == 1:
                        yield level - 1, 0, pos
                    elif dy == -1:
                        yield level - 1, pos, size - 1
                    elif dy == 1:
                        yield level - 1, pos, 0

    bugs = simulate_bugs(bugs, neighbors, part=2, n_minutes=n_minutes)
    return len(bugs)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2019, 24, "example")
    part1(parse(input))
