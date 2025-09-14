import sys
from collections import defaultdict

from aoc.util import timed

Graph = dict[str, set[str]]


def parse(input: str) -> Graph:
    graph = defaultdict(set)
    for line in input.splitlines():
        src, dst = line.split("-")
        graph[src].add(dst)
        graph[dst].add(src)
    return graph


def count_paths(graph: Graph, *, part2: bool) -> int:
    # Track visits only for small caves
    visits = {cave: 0 for cave in graph if cave.islower()}

    def backtrack(cave: str, used_double: bool = False) -> int:
        if cave == "end":
            return 1

        count = 0
        for next_cave in graph[cave]:
            if next_cave == "start":
                continue

            if next_cave not in visits:  # big cave
                count += backtrack(next_cave, used_double)
                continue

            # small cave
            match visits[next_cave]:
                case 0:
                    visits[next_cave] = 1
                    count += backtrack(next_cave, used_double)
                    visits[next_cave] = 0
                case 1 if part2 and not used_double:
                    visits[next_cave] = 2
                    count += backtrack(next_cave, True)
                    visits[next_cave] = 1
                case _:
                    continue

        return count

    return backtrack("start")


def part1(graph: Graph) -> int:
    return count_paths(graph, part2=False)


def part2(graph: Graph) -> int:
    return count_paths(graph, part2=True)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed})")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed})")


if __name__ == "__main__":
    main()
