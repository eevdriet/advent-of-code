import sys
from collections import defaultdict, deque

import parse as ps

from aoc.io import read_file
from aoc.util import timed

Coord = tuple[int, int]


def parse(input: str) -> dict[Coord, str]:
    filled = {}

    for line in input.splitlines():
        axis0, val0, _, start, end = ps.parse("{:w}={:d}, {:w}={:d}..{:d}", line)
        if axis0 == "x":
            x = val0
            for y in range(start, end + 1):
                filled[(x, y)] = "#"
        else:
            y = val0
            for x in range(start, end + 1):
                filled[(x, y)] = "#"
    return filled


class Tiles:
    def __init__(self):
        self.spring = (500, 1)
        self.filled = defaultdict(lambda: ".")

    def __str__(self):
        result = ""

        x_min = min(x for x, _ in self.filled)
        x_max = max(x for x, _ in self.filled)
        y_min = min(0, min(y for _, y in self.filled))
        y_max = max(y for _, y in self.filled)

        # Vertically plot the X coordinates
        for pow in reversed(range(1, 4)):
            result += " " * 5
            for x in range(x_min, x_max + 1):
                result += f"{(x % (10 ** pow)) // (10 ** (pow - 1))}"
            result += "\n"

        # Horizontally plot the Y coordinates with the cells themselves
        for y in range(y_min, y_max + 1):
            result += f"{y:04} "

            for x in range(x_min, x_max + 1):
                coord = (x, y)
                result += "+" if coord == self.spring else self.filled.get(coord, ".")

            result += "\n"

        return result

    def count(self, chars: str) -> int:
        clay_ys = [y for (_, y), tile in self.filled.items() if tile == "#"]
        y_min = min(clay_ys)
        y_max = max(clay_ys)

        return sum(
            1
            for ((_, y), tile) in self.filled.items()
            if y in range(y_min, y_max + 1) and tile in chars
        )

    def simulate(self, spring: Coord, filled: dict[Coord, str]):
        self.spring = spring
        self.filled = defaultdict(lambda: ".", filled)

        with open("out.txt", "w") as file:
            file.write(str(self))

        y_min = min(y for (_, y) in self.filled)
        y_max = max(y for (_, y) in self.filled)

        x, y = self.spring
        start = x, y + 1

        queue = deque([start])

        while queue:

            # Flow as far down as possible from the current spot
            x, y = queue.popleft()

            while y <= y_max and self.filled[(x, y)] in (".", "|"):
                self.filled[(x, y)] = "|"
                y += 1

            # Flow past the boundaries: go to the next source
            if y > y_max:
                continue

            # Try to fill the current level as much as possible
            y -= 1

            while True:
                # Try to flow as far to the left as possible
                left = x
                is_blocked_left = False

                while True:
                    # Boundary found: cannot flow further
                    if self.filled[(left - 1, y)] == "#":
                        is_blocked_left = True
                        break

                    # Flown as far left as possible before going down
                    if self.filled[(left - 1, y + 1)] in (".", "|"):
                        break

                    left -= 1

                # Do the same on the right side
                right = x
                is_blocked_right = False

                while True:
                    if self.filled[(right + 1, y)] == "#":
                        is_blocked_right = True
                        break

                    if self.filled[(right + 1, y + 1)] in (".", "|"):
                        break

                    right += 1

                # Block on both sides by #: fill the level with standing ~ water
                if is_blocked_left and is_blocked_right:
                    for xx in range(left, right + 1):
                        self.filled[(xx, y)] = "~"

                    # Continue if we can keep within the boundaries
                    if y <= y_min:
                        break
                    else:
                        y -= 1
                        continue

                # mark span flowing
                pass
                for xx in range(left, right + 1):
                    if self.filled[(xx, y)] != "#":
                        self.filled[(xx, y)] = "|"

                # enqueue spills
                if not is_blocked_left and self.filled[(left - 1, y)] != "|":
                    queue.append((left - 1, y))
                    self.filled[(left - 1, y)] = "|"

                if not is_blocked_right and self.filled[(right + 1, y)] != "|":
                    queue.append((right + 1, y))
                    self.filled[(right + 1, y)] = "|"

                break


def part1(clay: dict[Coord, str]) -> int:
    tiles = Tiles()
    tiles.simulate((500, 0), clay)

    return tiles.count("~|")


def part2(clay: dict[Coord, str]) -> int:
    tiles = Tiles()
    tiles.simulate((500, 0), clay)

    return tiles.count("~")


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2018, 17)
    print("Example Part 1:", part1(parse(input)))
