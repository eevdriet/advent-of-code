import collections
import enum
import sys
from copy import deepcopy
from dataclasses import dataclass
from itertools import count
from typing import NamedTuple

from aoc.constant import MISSING_INT
from aoc.util import timed


class Point(NamedTuple("Pt", [("x", int), ("y", int)])):
    def __add__(self, other):
        return type(self)(self.x + other.x, self.y + other.y)

    @property
    def nb4(self):
        return [
            self + d for d in [Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)]
        ]


class Team(enum.Enum):
    ELF = enum.auto()
    GOBLIN = enum.auto()


@dataclass
class Unit:
    team: Team
    position: Point
    hp: int = 200
    alive: bool = True
    power: int = 3


class ElfDiedException(Exception):
    pass


class Game(dict):
    def __init__(self):
        super().__init__()

        self.units: list[Unit] = []
        self.elf_death = False

    def score(self, n_rounds: int) -> int:
        return n_rounds * sum(unit.hp for unit in self.units if unit.alive)

    def play(self, elf_death=False, elf_power: int = 3) -> int:
        self.elf_death = elf_death

        # Set the power for every elf
        for unit in self.units:
            if unit.team == Team.ELF:
                unit.power = elf_power

        # Keep playing until no unit can move anymore
        for n_rounds in count(0):
            if self.round():
                return self.score(n_rounds)

        return MISSING_INT

    def round(self):
        units = sorted(self.units, key=lambda unit: unit.position)

        for unit in units:
            if not unit.alive:
                continue

            if self.move(unit):
                return True

    def move(self, unit: Unit):
        targets = [
            target for target in self.units if unit.team != target.team and target.alive
        ]
        occupied = set(u2.position for u2 in self.units if u2.alive and unit != u2)

        if not targets:
            return True

        in_range = set(
            pt
            for target in targets
            for pt in target.position.nb4
            if not self[pt] and pt not in occupied
        )

        if not unit.position in in_range:
            move = self.find_move(unit.position, in_range)

            if move:
                unit.position = move

        opponents = [
            target for target in targets if target.position in unit.position.nb4
        ]

        if opponents:
            target = min(opponents, key=lambda unit: (unit.hp, unit.position))

            target.hp -= unit.power

            if target.hp <= 0:
                target.alive = False
                if self.elf_death and target.team == Team.ELF:
                    raise ElfDiedException()

    def find_move(self, position, targets):
        visiting = collections.deque([(position, 0)])
        meta = {position: (0, None)}
        seen = set()
        occupied = {unit.position for unit in self.units if unit.alive}

        while visiting:
            pos, dist = visiting.popleft()
            for nb in pos.nb4:
                if self[nb] or nb in occupied:
                    continue
                if nb not in meta or meta[nb] > (dist + 1, pos):
                    meta[nb] = (dist + 1, pos)
                if nb in seen:
                    continue
                if not any(nb == visit[0] for visit in visiting):
                    visiting.append((nb, dist + 1))
            seen.add(pos)

        try:
            _, closest = min(
                (dist, pos) for pos, (dist, _) in meta.items() if pos in targets
            )
        except ValueError:
            return

        while meta[closest][0] > 1:
            closest = meta[closest][1]

        return closest


def parse(input: str) -> Game:
    game = Game()

    for i, line in enumerate(input.splitlines()):
        for j, el in enumerate(line):
            game[Point(i, j)] = el == "#"

            if el in "EG":
                game.units.append(
                    Unit(
                        team={"E": Team.ELF, "G": Team.GOBLIN}[el],
                        position=Point(i, j),
                        power={"E": 3, "G": 3}[el],
                    )
                )

    return game


def part1(game: Game) -> int:
    return game.play()


def part2(state: Game) -> int:
    # Try to play the game until an elf victory is guaranteed
    for power in count(4):
        try:
            game = deepcopy(state)
            outcome = game.play(elf_death=True, elf_power=power)
        except ElfDiedException:
            continue

        return outcome

    return MISSING_INT


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
