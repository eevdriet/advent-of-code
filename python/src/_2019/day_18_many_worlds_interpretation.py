import sys
from collections import deque
from heapq import heappop, heappush

from attrs import define

from aoc.io import read_file
from aoc.util import timed

Coord = tuple[int, int]


@define
class Map:
    map: dict[Coord, str]

    starts: dict[Coord, str]
    keys: dict[Coord, str]
    doors: dict[Coord, str]

    @classmethod
    def parse(cls, input: str) -> "Map":
        map = {
            (y, x): cell
            for y, row in enumerate(input.splitlines())
            for x, cell in enumerate(row)
        }

        # Collect interesting parts of the map
        starts = {
            coord: f"@{id}"
            for id, (coord, cell) in enumerate(map.items())
            if cell == "@"
        }

        keys = {
            coord: cell
            for coord, cell in map.items()
            if cell.isalpha() and cell.islower()
        }
        doors = {
            coord: cell
            for coord, cell in map.items()
            if cell.isalpha() and cell.isupper()
        }

        return cls(map, starts, keys, doors)

    def find_distances(self) -> dict[tuple[Coord, Coord], tuple[int, set[str]]]:
        distances = {}

        def bfs(start: Coord):
            seen = set([start])
            queue = deque([(start, 0, frozenset())])  # use immutable set

            while queue:
                coord, n_steps, path_doors = queue.popleft()

                if coord in keys:
                    distances[(start, coord)] = (n_steps, path_doors)
                    distances[(coord, start)] = (n_steps, path_doors)

                if coord in self.doors:
                    door = self.map[coord]
                    path_doors = path_doors | {door}  # make a new frozenset

                x, y = coord
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    next_coord = (x + dx, y + dy)
                    if self.map.get(next_coord, "#") == "#":
                        continue
                    if next_coord in seen:
                        continue
                    seen.add(next_coord)
                    queue.append((next_coord, n_steps + 1, path_doors))

        keys = {**self.starts, **self.keys}
        for coord in keys.keys():
            bfs(coord)

        return distances

    def collect_keys(self):
        # Perform a BFS to store the minimal distance between keys, as well as which doors are encountered
        distances = self.find_distances()

        start_coords = tuple(self.starts.keys())
        prio_queue = [(0, start_coords, frozenset())]
        seen = set()

        while prio_queue:
            n_steps, coords, keys = heappop(prio_queue)

            if len(keys) == len(self.keys):
                return n_steps

            if (coords, keys) in seen:
                continue
            seen.add((coords, keys))

            for idx, coord in enumerate(coords):
                for next_coord in self.keys:
                    # Should not go back to key that is already picked up
                    next_key = self.keys[next_coord]
                    if next_key in keys:
                        continue

                    # Cannot go to unreachable position
                    edge = (coord, next_coord)
                    if edge not in distances:
                        continue

                    # Cannot go to a key if we don't have the required doors
                    distance, doors = distances[edge]
                    if any(door.lower() not in keys for door in doors):
                        continue

                    next_coords = list(coords)
                    next_coords[idx] = next_coord

                    state = n_steps + distance, tuple(next_coords), keys | {next_key}
                    heappush(prio_queue, state)

        raise RuntimeError(f"Cannot find shortest path for {map}")


def parse(input: str) -> Map:
    return Map.parse(input)


def part1(map: Map) -> int:
    return map.collect_keys()


def part2(map: Map) -> int:
    # Replace starts if needed
    if len(map.starts) == 1:
        x, y = next(iter(map.starts.keys()))

        # Place starts along the x of the original start
        map.starts = {
            (x + dx, y + dy): f"@{idx}"
            for idx, (dx, dy) in enumerate([(-1, -1), (-1, 1), (1, -1), (1, 1)])
        }

        # Replace the + of free spaces around the original start with walls
        for idx, (dx, dy) in enumerate([(-1, 0), (0, 0), (1, 0), (0, -1), (0, 1)]):
            map.map[(x + dx, y + dy)] = "#"

    return map.collect_keys()


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2019, 18, "example1")
    part1(parse(input))
