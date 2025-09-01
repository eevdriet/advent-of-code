import sys
from collections import defaultdict

from aoc.util import timed

Graph = dict[int, set[int]]


def parse(input: str) -> Graph:
    graph = defaultdict(set)

    for line in input.splitlines():
        source, destinations = line.split(" <-> ")

        for dest in destinations.split(", "):
            graph[int(source)].add(int(dest))

    return graph


def part1(graph: Graph) -> int:
    group = set()

    def dfs(node: int):
        if node in group:
            return

        group.add(node)

        for neighbor in graph[node]:
            dfs(neighbor)

    dfs(0)
    return len(group)


def part2(graph: Graph) -> int:
    n_nodes = len(graph)
    n_groups = 0

    found = set()
    group = set()

    def dfs(node: int):
        if node in group:
            return

        group.add(node)

        for neighbor in graph[node]:
            dfs(neighbor)

    while len(found) < n_nodes:
        for node in graph:
            if node in found:
                continue

            dfs(node)
            found |= group
            n_groups += 1

    return n_groups


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
