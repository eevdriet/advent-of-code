from aoc.io import FileType, open_file
from aoc.util import Point, pairwise_sum

YEAR = 2024
DAY = 6


class Grid:
    def __init__(self, width: int, height: int, obstacles: set[Point], start: Point):
        self.width = width
        self.height = height
        self.obstacles = obstacles
        self.start = start

    @classmethod
    def parse(cls, rows: list[str]):
        height = len(rows)
        width = len(rows[0])
        obstacles: set[Point] = set()

        for r, row in enumerate(rows):
            for c, cell in enumerate(row):
                pos = (r, c)

                match cell:
                    case "^":
                        start = pos
                    case "#":
                        obstacles.add(pos)

        return Grid(width, height, obstacles, start)

    def n_visited_positions(self) -> int:
        pos = self.start
        dir = (-1, 0)
        visited = {(pos)}

        while 0 <= pos[0] < self.width and 0 <= pos[1] < self.height:
            new_pos = pairwise_sum(dir, pos)

            if new_pos in self.obstacles:
                dir = (-dir[1], dir[0])
            else:
                pos = new_pos
                visited.add(pos)

        return len(visited) - 1

    def n_looping_obstacles(self) -> int:
        def detect_loop() -> bool:
            pos = self.start
            dir = (-1, 0)
            visited = {(pos, dir)}

            while 0 <= pos[0] < self.height and 0 <= pos[1] < self.width:
                new_pos = pairwise_sum(dir, pos)

                if new_pos in self.obstacles:
                    dir = (dir[1], -dir[0])
                else:
                    pos = new_pos

                key = (pos, dir)
                if key in visited:
                    return True

                visited.add(key)

            return False

        n_extra_obstacles = 0

        for r in range(self.height):
            for c in range(self.width):
                pos = (r, c)
                if pos in self.obstacles or pos == self.start:
                    continue

                self.obstacles.add(pos)
                n_extra_obstacles += detect_loop()
                self.obstacles.remove(pos)

        return n_extra_obstacles


def main():
    with open_file(YEAR, DAY, FileType.INPUT) as file:
        lines = file.read().splitlines()
        grid = Grid.parse(lines)

    # print(f"Part 1: {grid.n_visited_positions()}")
    print(f"Part 2: {grid.n_looping_obstacles()}")


if __name__ == "__main__":
    main()
