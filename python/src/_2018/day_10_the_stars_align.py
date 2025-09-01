import re
import sys
from collections import Counter

import numpy as np

from aoc.io import open_file
from aoc.util import timed


def parse(input: str) -> list[list[int]]:
    return [
        [int(num) for num in re.findall(r"(-?\d+)", line)]
        for line in input.splitlines()
    ]


def part1(nums: list[list[int]]) -> tuple[str, int]:
    # Initialize coordinates and velocities
    array = np.array(nums)
    coords = array[:, :2].copy()
    velos = array[:, 2:].copy()

    # Determine which time produces the smallest bounding box
    box_coords = coords.copy()
    time = 0
    min_area = sys.maxsize
    min_time = -1

    for time in range(20_000):
        box_coords += velos
        time += 1

        # Find boundaries of points
        x_min = min(box_coords[:, 0])
        y_min = min(box_coords[:, 1])
        x_max = max(box_coords[:, 0])
        y_max = max(box_coords[:, 1])

        area = (x_max - x_min + 1) * (y_max - y_min + 1)
        if area < min_area:
            min_area = area
            min_time = time

    assert min_time >= 0

    # Then simulate back to that time and print the word
    coords += min_time * velos

    # Find boundaries of points
    x_min = min(coords[:, 0])
    y_min = min(coords[:, 1])
    x_max = max(coords[:, 0])
    y_max = max(coords[:, 1])

    # If all points are contained within certain bounds, find the word
    word = ""

    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            target = np.array([x, y])
            word += "#" if np.any(np.all(coords == target, axis=1)) else "."

        word += "\n"

    return word, min_time


def part2(nums: list[list[int]]) -> int:
    return 0


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    with open_file(2018, 10) as file:
        print(part1(parse(file.read())))
