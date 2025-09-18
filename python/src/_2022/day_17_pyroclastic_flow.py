import sys

from aoc.util import timed

Rock = tuple[complex, ...]

ROCKS: list[Rock] = [
    (0, 1, 2, 3),
    (1, 0 + 1j, 2 + 1j, 1 + 2j),
    (0, 1, 2, 2 + 1j, 2 + 2j),
    (0, 0 + 1j, 0 + 2j, 0 + 3j),
    (0, 1, 0 + 1j, 1 + 1j),
]

ROCK_HEIGHTS = [1, 3, 3, 4, 2]
JET_MOVES = {"<": -1, ">": 1}


def parse(input: str) -> list[str]:
    return [jet for jet in input.strip()]


def drop_rocks(jets: list[str], *, n_steps: int) -> int:
    tower = set()
    cache = {}
    top = 0

    rock_idx = 0
    jet_idx = 0

    def is_empty(pos: complex) -> bool:
        return pos.real in range(7) and pos.imag > 0 and pos not in tower

    def check(pos: complex, dir: complex, rock: Rock) -> bool:
        return all(is_empty(pos + dir + r) for r in rock)

    for step in range(n_steps):
        pos = complex(2, top + 4)  # set start pos

        key = rock_idx, jet_idx
        if key in cache and step > 1000:  # check for cycle
            S, T = cache[key]
            d, m = divmod(n_steps - step, step - S)
            if m == 0:
                return top + (top - T) * d
        else:
            cache[key] = step, top

        rock = ROCKS[rock_idx]  # get next rock
        rock_idx = (rock_idx + 1) % len(ROCKS)  # and inc index

        while True:
            jet = JET_MOVES[jets[jet_idx]]  # get next jet
            jet_idx = (jet_idx + 1) % len(jets)  # and inc index

            if check(pos, jet, rock):
                pos += jet  # maybe move side
            if check(pos, -1j, rock):
                pos += -1j  # maybe move down
            else:
                break  # can't move down

        tower |= {pos + r for r in rock}  # add rock to tower
        top = max(top, int(pos.imag) + [1, 0, 2, 2, 3][rock_idx])  # compute new top

    return top


def part1(jets: list[str]) -> int:
    return drop_rocks(jets, n_steps=2022)


def part2(jets: list[str]) -> int:
    return drop_rocks(jets, n_steps=1_000_000_000_000)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
