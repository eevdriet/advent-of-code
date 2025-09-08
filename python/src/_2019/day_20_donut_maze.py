import sys
from collections import defaultdict, deque

from attrs import define

from aoc.io import read_file
from aoc.util import timed

Coord = tuple[int, int]


@define
class Maze:
    tiles: dict[Coord, str]
    portals: dict[str, list[Coord]]
    dim: tuple[int, int]

    @classmethod
    def parse(cls, text: str) -> "Maze":
        # Parse all cells first to index easily later on
        cells = [list(row) for row in text.splitlines()]
        y_max = len(cells)
        x_max = len(cells[0])

        # Find open tiles
        tiles: dict[Coord, str] = {}

        for y in range(y_max):
            for x in range(x_max):
                if cells[y][x] == ".":
                    tiles[(x, y)] = "."

        # Detect the portals
        portals: dict[str, list[Coord]] = defaultdict(list)

        for y in range(y_max):
            for x in range(x_max):
                if not cells[y][x].isalpha():
                    continue

                # Horizontal
                if x + 1 < x_max and cells[y][x + 1].isalpha():
                    portal = cells[y][x] + cells[y][x + 1]

                    # Left portals
                    if x - 1 >= 0 and cells[y][x - 1] == ".":
                        portals[portal].append((x - 1, y))

                    # Right portals
                    elif x + 2 < x_max and cells[y][x + 2] == ".":
                        portals[portal].append((x + 2, y))

                # Vertical
                if y + 1 < y_max and cells[y + 1][x].isalpha():
                    portal = cells[y][x] + cells[y + 1][x]

                    # Top portals
                    if y - 1 >= 0 and cells[y - 1][x] == ".":
                        portals[portal].append((x, y - 1))

                    # Bottom portals
                    elif y + 2 < y_max and cells[y + 2][x] == ".":
                        portals[portal].append((x, y + 2))

        return cls(tiles, portals, (x_max, y_max))


def parse(input: str) -> Maze:
    return Maze.parse(input)


def part1(maze: Maze) -> int:
    start = maze.portals["AA"][0]
    goal = maze.portals["ZZ"][0]

    queue = deque([(start, 0)])
    seen = {start}

    while queue:
        (x, y), dist = queue.popleft()
        if (x, y) == goal:
            return dist

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ncoord = (x + dx, y + dy)
            if ncoord in maze.tiles and ncoord not in seen:
                seen.add(ncoord)
                queue.append((ncoord, dist + 1))

        # teleport if this coordinate is a portal
        for label, coords in maze.portals.items():
            if (x, y) in coords and label not in ("AA", "ZZ"):
                # jump to the other end
                other = coords[0] if coords[1] == (x, y) else coords[1]
                if other not in seen:
                    seen.add(other)
                    queue.append((other, dist + 1))

    raise RuntimeError("no path found")


def part2(maze: Maze) -> int:
    start = maze.portals["AA"][0]
    goal = maze.portals["ZZ"][0]

    queue = deque([(start, 0, 0)])
    seen = {(start, 0)}
    x_max, y_max = maze.dim

    while queue:
        (x, y), floor, dist = queue.popleft()
        if (x, y) == goal and floor == 0:
            return dist

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ncoord = (x + dx, y + dy)
            state = (ncoord, floor)

            if ncoord in maze.tiles and state not in seen:
                seen.add(state)
                queue.append((ncoord, floor, dist + 1))

        # teleport if this coordinate is a portal
        for src, coords in maze.portals.items():
            if (x, y) in coords and src not in ("AA", "ZZ"):
                dst = coords[0] if coords[1] == (x, y) else coords[1]

                is_outer = x in (2, x_max - 3) or y in (2, y_max - 3)
                next_floor = floor - 1 if is_outer else floor + 1

                if next_floor >= 0:
                    state = (dst, next_floor)

                    if state not in seen:
                        seen.add(state)
                        queue.append((dst, next_floor, dist + 1))

    raise RuntimeError("no path found")


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2019, 20)
    part1(parse(input))
