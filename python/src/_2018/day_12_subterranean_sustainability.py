import sys

from aoc.io import open_file
from aoc.util import timed


def parse(input: str) -> tuple[str, dict[str, str]]:
    """
    initial state: #...####.##..####..#.##....##...###.##.#..######..#..#..###..##.#.###.#####.##.#.#.#.##....#..#..#..

    ...## => .
    ...#. => #
    ....# => .
    """
    state_line, behavior_lines = input.strip().split("\n\n")
    state = state_line.strip().split(": ")[1]

    behavior = {}
    for line in behavior_lines.splitlines():
        src, dst = line.split(" => ")
        if dst == "#":
            behavior[src] = dst

    return state, behavior


def grow_plants(plants: str, behavior: dict[str, str], n_generations: int) -> int:
    curr = {idx for idx, plant in enumerate(plants) if plant == "#"}
    seen = {}

    gen = 0

    while gen < n_generations:
        # Produce next generation
        gen += 1
        next = set()

        left = min(curr)
        right = max(curr)

        for start in range(left - 3, right + 4):
            state = "".join(
                "#" if start + step in curr else "." for step in range(-2, 3)
            )
            if state in behavior:
                next.add(start)

        curr = next

        # Normalize plants shape and determine whether it is seen before
        shape = tuple(sorted(plant - left for plant in curr))

        if shape not in seen:
            seen[shape] = (gen, left)
            continue

        # If so, we can skip ahead by however long the cycle is
        prev_gen, prev_left = seen[shape]
        cycle_len = gen - prev_gen
        cycle_shift = left - prev_left

        # Reset the current state and generation
        n_remaining = n_generations - gen
        n_skipped_cycles = n_remaining // cycle_len

        shift = cycle_shift * n_skipped_cycles
        curr = {plant + shift for plant in curr}
        gen += cycle_len * n_skipped_cycles

    return sum(curr)


def part1(plants: str, behavior: dict[str, str]) -> int:
    return grow_plants(plants, behavior, 20)


def part2(plants: str, behavior: dict[str, str]) -> int:
    return grow_plants(plants, behavior, 50_000_000_000)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, *parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    with open_file(2018, 12, "example") as file:
        part1(*parse(file.read()))
