import sys
from itertools import count

from aoc.io import open_file
from aoc.util import timed

Layer = tuple[int, int]


def parse(input: str) -> list[Layer]:
    return [tuple(map(int, line.split(": "))) for line in input.splitlines()]


def part1(layers: list[Layer]) -> int:
    severity = 0

    for depth, _range in layers:
        n_steps = 2 * (_range - 1)
        if depth % n_steps == 0:
            severity += depth * _range

    return severity


def part2(layers: list[Layer]) -> int:
    def is_safe(layer: Layer, delay: int) -> bool:
        depth, _range = layer
        n_steps = 2 * (_range - 1)

        return (depth + delay) % n_steps != 0

    return next(
        (sec for sec in count() if all(is_safe(layer, sec) for layer in layers)), -1
    )


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    with open_file(2017, 13, name="example") as file:
        part1(parse(file.read()))
