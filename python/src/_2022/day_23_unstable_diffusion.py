import sys
from collections import defaultdict, deque

from aoc.io import read_file
from aoc.util import adjacent8, timed


def parse(input: str) -> set[complex]:
    return {
        x + y * 1j
        for y, line in enumerate(input.splitlines())
        for x, cell in enumerate(line)
        if cell == "#"
    }


Elf = complex


def move_elves(elves: set[Elf], *, n_rounds: int, stop_without_movement: bool) -> int:
    directions: deque[tuple[complex, list[int]]] = deque(
        [(-1j, [0, 1, 2]), (+1j, [5, 6, 7]), (-1, [0, 3, 5]), (+1, [2, 4, 7])]
    )

    for round in range(n_rounds):
        # Part 1a: determine which elves stay put
        elf_neighbors = {
            elf: [bool(neighbor in elves) for neighbor in adjacent8(elf)]
            for elf in elves
        }

        stay_put = {elf for elf in elves if sum(elf_neighbors[elf]) == 0}
        if stop_without_movement and len(stay_put) == len(elves):
            return round + 1

        # Part 1b: determine where all moving elves want to move to
        destination_counts = defaultdict(int)

        elf_destinations = {}
        for elf in elves - stay_put:
            neighbors = elf_neighbors[elf]

            for dir, indices in directions:
                if all(not neighbors[idx] for idx in indices):
                    destination = elf + dir
                    elf_destinations[elf] = destination
                    destination_counts[destination] += 1
                    break
            else:
                stay_put.add(elf)

        # Part 2a: move all elves
        new_elves = set(stay_put)

        for elf, destination in elf_destinations.items():
            if destination_counts[destination] == 1:
                new_elves.add(destination)
            else:
                new_elves.add(elf)

        # Part 2b: shift the direction to consider
        elves = new_elves
        directions.rotate(-1)

    x_min = int(min(elf.real for elf in elves))
    x_max = int(max(elf.real for elf in elves))
    y_min = int(min(elf.imag for elf in elves))
    y_max = int(max(elf.imag for elf in elves))

    n_tiles = (x_max - x_min + 1) * (y_max - y_min + 1)
    n_filled_tiles = len(elves)

    return n_tiles - n_filled_tiles


def part1(elves: set[Elf]) -> int:
    return move_elves(elves, n_rounds=10, stop_without_movement=False)


def part2(elves: set[Elf]) -> int:
    return move_elves(elves, n_rounds=1_000_000, stop_without_movement=True)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    example = read_file(2022, 23, "example1")
    result = part1(parse(example))
    pass
