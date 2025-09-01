import sys
from collections import defaultdict

import numpy as np
import parse as ps
from attrs import define

from aoc.io import open_file
from aoc.util import timed

Vec3 = np.array


@define
class Particle:
    id: str
    pos: np.typing.NDArray = np.array([0, 0, 0])
    velo: np.typing.NDArray = np.array([0, 0, 0])
    accel: np.typing.NDArray = np.array([0, 0, 0])

    @classmethod
    def parse(cls, id: str, line: str) -> "Particle":
        match = ps.parse(
            "p=<{px:d},{py:d},{pz:d}>, v=<{vx:d},{vy:d},{vz:d}>, a=<{ax:d},{ay:d},{az:d}>",
            line,
        )

        pos = np.array([match["px"], match["py"], match["pz"]])
        velo = np.array([match["vx"], match["vy"], match["vz"]])
        accel = np.array([match["ax"], match["ay"], match["az"]])

        return cls(id, pos, velo, accel)

    def update(self):
        self.velo += self.accel
        self.pos += self.velo

    def dist(self, other: "Particle") -> int:
        return sum(
            abs(axis - other_axis) for axis, other_axis in zip(self.pos, other.pos)
        )

    def __hash__(self):
        return hash(self.id)


def parse(input: str) -> list[Particle]:
    return [Particle.parse(str(id), line) for id, line in enumerate(input.splitlines())]


def part1(particles: list[Particle]) -> str:
    origin = Particle("origin")

    for _ in range(500):
        for particle in particles:
            particle.update()

    closest = min(particles, key=lambda p: p.dist(origin))
    return closest.id


def part2(particles: list[Particle]) -> int:
    n_iters_no_collision = 0
    remaining = set(particles)

    while len(remaining) > 0 and n_iters_no_collision < 50:
        removed_particles = False
        positions = defaultdict(set)

        for particle in remaining:
            positions[tuple(particle.pos)].add(particle)
            particle.update()

        for _, parts in positions.items():
            if len(parts) > 1:
                removed_particles = True
                remaining.difference_update(parts)

        if not removed_particles:
            n_iters_no_collision += 1

    return len(remaining)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    with open_file(2017, 20) as file:
        part2(parse(file.read()))
