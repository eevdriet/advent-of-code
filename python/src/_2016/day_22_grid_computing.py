import re
import sys
from collections import deque

from aoc.io import open_file
from aoc.util import timed


class Node:
    """
    root@ebhq-gridcenter# df -h
    Filesystem              Size  Used  Avail  Use%
    /dev/grid/node-x0-y0     90T   69T    21T   76%
    /dev/grid/node-x0-y1     88T   71T    17T   80%
    /dev/grid/node-x0-y2     92T   64T    28T   69%
    """

    def __init__(self, x: int, y: int, size: int, used: int):
        self.x = x
        self.y = y

        self.size = size
        self.used = used

    @classmethod
    def parse(cls, line: str) -> "Node":
        x, y, size, used, *_ = (int(num) for num in re.findall(r"(\d+)", line))
        return cls(x, y, size, used)

    @property
    def available(self):
        assert self.size - self.used
        return self.size - self.used

    def can_move(self, other: "Node") -> bool:
        return self.used > 0 and self.used < other.available

    def move(self, other: "Node"):
        other.used += self.size

    def __hash__(self) -> int:
        return hash((self.x, self.y))


def parse(input: str) -> list[Node]:
    return [Node.parse(line) for line in input.splitlines()[2:]]


def create_grid(nodes: list[Node]) -> str:
    max_x = max(nodes, key=lambda node: node.x).x
    max_y = max(nodes, key=lambda node: node.y).y

    grid = [[""] * (max_x + 1) for _ in range(max_y + 1)]

    for node in nodes:
        grid[node.y][node.x] = f"{node.used if node.used else "___":<3}/{node.size}"

    return "\n".join(
        "".join(grid[row][col].ljust(10) for col in range(max_x + 1))
        for row in range(max_y + 1)
    )


def part1(nodes: list[Node]) -> int:
    n_pairs = 0

    for left, first in enumerate(nodes):
        for second in nodes[left + 1 :]:
            n_pairs += first.can_move(second)
            n_pairs += second.can_move(first)

    return n_pairs


def part2(node_list: list[Node]) -> int:
    nodes = {(node.x, node.y): node for node in node_list}

    def dist(src: Node, dst: Node) -> int:
        return abs(src.x - dst.x) + abs(src.y - dst.y)

    # Inspect the input to find where all the nodes of interest are
    goal = nodes[(34, 0)]
    empty = nodes[(3, 20)]

    a = nodes[(0, 7)]
    b = nodes[(goal.x - 1, goal.y)]
    c = nodes[(0, 0)]

    # We move one extra space to get past the wall from the gap
    return 1 + dist(empty, a) + dist(a, b) + 5 * dist(b, c)


if __name__ == "__main__":
    # input = sys.stdin.read()
    # parsed = parse(input)
    #
    # result1, elapsed = timed(part1, parsed)
    # print(f"Part 1: {result1} ({elapsed} elapsed)")
    #
    # result2, elapsed = timed(part2, parsed)
    # print(f"Part 2: {result2} ({elapsed} elapsed)")

    with open_file(2016, 22) as file:
        nodes = parse(file.read())

    print(create_grid(nodes))
