import re
import sys
from copy import deepcopy
from math import lcm

import numpy as np
from attrs import define, field

from aoc.io import read_file
from aoc.util import timed


@define(hash=True)
class Moon:
    pos: np.typing.NDArray
    vel: np.typing.NDArray = field(factory=lambda: np.array([0, 0, 0]))

    @property
    def energy(self):
        return np.absolute(self.pos).sum() * np.absolute(self.vel).sum()


def parse(input: str) -> list[Moon]:
    return [
        Moon(np.array([*map(int, re.findall(r"(-?\d+)", line))]))
        for line in input.splitlines()
    ]


def apply_gravity(moons: list[Moon], axis: int):
    for left in range(len(moons)):
        for right in range(left + 1, len(moons)):
            lpos = moons[left].pos[axis]
            rpos = moons[right].pos[axis]

            if lpos > rpos:
                moons[left].vel[axis] -= 1
                moons[right].vel[axis] += 1
            elif rpos > lpos:
                moons[right].vel[axis] -= 1
                moons[left].vel[axis] += 1


def simulate(moons: list[Moon], n_steps: int):
    for _ in range(n_steps):
        # Apply gravity
        for axis in range(3):
            apply_gravity(moons, axis)

        pass

        # Apply velocity
        for moon in moons:
            moon.pos += moon.vel


def part1(moons: list[Moon]) -> int:
    simulate(moons, 1000)

    return int(sum(moon.energy for moon in moons))


def part2(orig_moons: list[Moon]) -> int:
    # Determine for each axis separately when it cycles
    cycle_lens = [0] * 3

    for axis in range(3):
        orig_key = tuple((moon.pos[axis], moon.vel[axis]) for moon in orig_moons)
        key = None

        moons = deepcopy(orig_moons)
        n_cycles = 0

        while key != orig_key:
            n_cycles += 1

            simulate(moons, 1)
            key = tuple((moon.pos[axis], moon.vel[axis]) for moon in moons)

        cycle_lens[axis] = n_cycles

    return lcm(*cycle_lens)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2019, 12, "example1")
    part2(parse(input))
