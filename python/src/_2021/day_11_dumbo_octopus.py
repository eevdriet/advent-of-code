import sys

from aoc.util import adjacent8, timed

Octupuses = dict[complex, int]


def parse(input: str) -> Octupuses:
    return {
        complex(x, y): int(energy)
        for y, row in enumerate(input.splitlines())
        for x, energy in enumerate(row)
    }


def simulate(
    octopuses: Octupuses, *, n_steps: int, stop_at_simultaneous_flashes: bool = False
) -> int:
    n_flashes = 0

    for step in range(1, n_steps + 1):
        flashed = []

        # Increase the energy of all octopuses and register those who should flash
        for octopus in octopuses:
            octopuses[octopus] += 1

            if octopuses[octopus] > 9:
                flashed.append(octopus)

        while flashed:
            octopus = flashed.pop()

            # Octopus flashed before: ignore
            if octopuses[octopus] == 0:
                continue

            # Octopus flashes: increase neighbors energy
            octopuses[octopus] = 0
            n_flashes += 1

            for neighbor in adjacent8(octopus):
                # Ignore neighbor if it is OOB or flashed before
                if neighbor not in octopuses or octopuses[neighbor] == 0:
                    continue

                # Otherwise, let the neighbor flash as well
                octopuses[neighbor] += 1
                if octopuses[neighbor] > 9:
                    flashed.append(neighbor)

        # If required, the result is the step all octopuses first flash simultaneously
        if stop_at_simultaneous_flashes and all(
            energy == 0 for energy in octopuses.values()
        ):
            return step

    # Otherwise, it is the total number of flashes depending on how many steps were performed
    return n_flashes


def part1(octupuses: Octupuses) -> int:
    return simulate(octupuses, n_steps=100)


def part2(octupuses: Octupuses) -> int:
    return simulate(octupuses, n_steps=sys.maxsize, stop_at_simultaneous_flashes=True)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
