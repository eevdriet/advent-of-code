import sys
from itertools import pairwise, permutations
from typing import TextIO

import parse as ps

City = str
Distances = dict[tuple[City, City], int]


def parse(input: str) -> tuple[Distances, set[City]]:
    distances = {}
    cities = set()

    for line in input.splitlines():
        src, dst, dist = ps.parse("{} to {} = {:d}", line)

        distances[(src, dst)] = dist
        distances[(dst, src)] = dist

        cities.add(src)
        cities.add(dst)

    return distances, cities


def find_minmax_route(distances: Distances, cities: set[City]) -> tuple[int, int]:
    min_dist = sys.maxsize
    max_dist = -sys.maxsize

    for route in permutations(cities):
        dist = sum(distances[(src, dst)] for src, dst in pairwise(route))

        min_dist = min(dist, min_dist)
        max_dist = max(dist, max_dist)

    return min_dist, max_dist


def part1(distances: Distances, cities: set[City]):
    min_dist, _ = find_minmax_route(distances, cities)

    return min_dist


def part2(distances: Distances, cities: set[City]):
    _, max_dist = find_minmax_route(distances, cities)

    return max_dist


def main():
    input = sys.stdin.read()
    distances, cities = parse(input)

    min_dist, max_dist = find_minmax_route(distances, cities)

    print(f"Part 1: {min_dist}")
    print(f"Part 2: {max_dist}")


if __name__ == "__main__":
    main()
