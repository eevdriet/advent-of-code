import sys
from math import ceil, floor, sqrt

from aoc.util import timed
from aoc.util.re import find_nums


def parse(input: str) -> tuple[list[int], list[int]]:
    times_line, distances_line = input.splitlines()

    return find_nums(times_line), find_nums(distances_line)


def count_winning_ways(times: list[int], distances: list[int]) -> int:
    total = 1

    def count1(n_seconds: int, dist: int) -> int:
        # Use the abc-formula to find intersection points
        start = None
        stop = None

        for n_waits in range(1, n_seconds):
            if n_waits * (n_seconds - n_waits) > dist:
                if start is None:
                    start = n_waits
            else:
                if start is not None and stop is None:
                    stop = n_waits
                    break

        assert start is not None
        assert stop is not None

        return stop - start

    def count2(n_seconds: int, dist: int) -> int:
        b2 = n_seconds**2
        _4ac = 4 * dist

        if b2 < _4ac:
            return 0

        descriminant = sqrt(b2 - _4ac)
        t1 = (n_seconds - descriminant) / 2
        t2 = (n_seconds + descriminant) / 2

        low = ceil(t1 + 1e-9)
        high = floor(t2 - 1e-9)

        return high - low + 1

    for n_seconds, max_dist in zip(times, distances):
        total *= count2(n_seconds, max_dist)

    return total


def part1(times: list[int], distances: list[int]) -> int:
    return count_winning_ways(times, distances)


def part2(times: list[int], distances: list[int]) -> int:
    time = int("".join(str(time) for time in times))
    dist = int("".join(str(dist) for dist in distances))

    return count_winning_ways([time], [dist])


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, *parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
