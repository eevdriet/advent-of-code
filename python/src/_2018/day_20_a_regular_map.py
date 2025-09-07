import sys

import networkx

from aoc.util import timed

Coord2D = tuple[int, int]
Nodes = dict[int, str]
Edges = dict[Coord2D, set[Coord2D]]

DIRS = {
    "N": 1j,
    "S": -1j,
    "E": 1,
    "W": -1,
}


def parse(regex: str) -> networkx.Graph:
    regex = regex.strip("^$")
    graph = networkx.Graph()

    stack = []

    curr = {0}
    starts = {(0, 0)}
    ends = set()

    for chr in regex:
        match chr:
            case c if c in DIRS:
                dir = DIRS[chr]
                graph.add_edges_from((coord, coord + dir) for coord in curr)
                curr = {coord + dir for coord in curr}
            case "(":
                stack.append((starts, ends))
                starts = curr
                ends = set()
            case ")":
                curr.update(ends)
                starts, ends = stack.pop()
            case "|":
                ends.update(curr)
                curr = starts
            case _:
                raise ValueError(f"unexpected {chr}")

    return graph


def part1(graph: networkx.Graph) -> int:
    paths = networkx.algorithms.shortest_path_length(graph, 0)
    return max(paths.values())


def part2(graph: networkx.Graph) -> int:
    paths = networkx.algorithms.shortest_path_length(graph, 0)
    return sum(1 for path_len in paths.values() if path_len >= 1000)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    part1(*parse("^ENWWW(NEEE|SSE(EE|N))$"))
