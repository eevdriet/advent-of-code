import re
import sys
from copy import deepcopy
from itertools import count
from typing import Optional

from attrs import define, field

from aoc.io import read_file
from aoc.util import timed


@define
class Group:
    id: str
    n_units: int
    unit_hp: int

    attack_damage: int
    attack_type: str
    initiative: int

    weaknesses: set[str] = field(factory=lambda: set())
    immunities: set[str] = field(factory=lambda: set())

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"

    @property
    def effective_power(self):
        return self.n_units * self.attack_damage

    def is_alive(self) -> bool:
        return self.n_units > 0

    def power_against(self, other: "Group") -> int:
        if self.attack_type in other.immunities:
            return 0
        elif self.attack_type in other.weaknesses:
            return 2 * self.effective_power
        else:
            return self.effective_power


@define
class System:
    id: str
    groups: list[Group]

    @property
    def n_units(self):
        return sum(group.n_units for group in self.groups)

    def is_alive(self) -> bool:
        return any(group.is_alive() for group in self.groups)

    def select_targets(self, other: "System") -> dict[Group, Optional[Group]]:
        target_groups = {group for group in other.groups if group.is_alive()}
        targets = {}

        groups = sorted(
            self.groups,
            key=lambda group: (group.effective_power, group.initiative),
            reverse=True,
        )
        for group in groups:
            target = max(
                target_groups,
                key=lambda t: (group.power_against(t), t.effective_power, t.initiative),
                default=None,
            )

            if target is not None and group.power_against(target) > 0:
                targets[group] = target
                target_groups.remove(target)

        return targets


def parse(input: str) -> tuple[System, System]:
    imm_text, inf_text = input.strip().split("\n\n")

    def parse_system(text: str) -> System:
        id_line, *lines = text.splitlines()
        id = id_line.split(":")[0]

        groups = []
        for idx, line in enumerate(lines, start=1):
            # Parse the group's description
            match = re.match(
                r"(\d+) units each with (\d+) hit points(?: \((.*)\))? with an attack that does (\d+) (\w+) damage at initiative (\d+)",
                line,
            )
            if not match:
                raise ValueError(f"Group description is invalid: {line}")

            n_units, hit_points, extra, damage, attack_typ, initiative = match.groups()

            # Determine the weaknesses and immunities separately
            weaknesses = set()
            immunities = set()

            if extra:
                for part in extra.split("; "):
                    typ, _, *traits = re.split(r",? ", part)
                    match typ:
                        case "weak":
                            weaknesses |= set(traits)
                        case "immune":
                            immunities |= set(traits)

            # Create group
            group = Group(
                f"{id}-{idx}",
                int(n_units),
                int(hit_points),
                int(damage),
                attack_typ,
                int(initiative),
                weaknesses,
                immunities,
            )
            groups.append(group)

        return System(id, groups)

    return parse_system(imm_text), parse_system(inf_text)


def simulate(immunes: System, infection: System) -> None:
    while immunes.is_alive() and infection.is_alive():
        # Select the targets for both systems
        targets = immunes.select_targets(infection)
        targets |= infection.select_targets(immunes)

        # Attack in order of initiative
        groups = sorted(targets.keys(), key=lambda g: g.initiative, reverse=True)
        any_units_killed = False

        for group in groups:
            target = targets[group]

            if target is None or not (group.is_alive() and target.is_alive()):
                continue

            n_units_killed = min(
                target.n_units, group.power_against(target) // target.unit_hp
            )
            target.n_units -= n_units_killed

            if n_units_killed > 0:
                any_units_killed = True

        if not any_units_killed:
            break


def part1(immunes: System, infection: System) -> int:
    simulate(immunes, infection)

    return max(0, immunes.n_units) + max(0, infection.n_units)


def part2(immunes: System, infection: System) -> int:
    for boost in count(1):
        imm = deepcopy(immunes)
        inf = deepcopy(infection)

        # Apply the boost to the immune group
        for group in imm.groups:
            group.attack_damage += boost

        simulate(imm, inf)

        if imm.is_alive() and not inf.is_alive():
            return imm.n_units

    raise RuntimeError("No boost lets the immunes win")


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, *parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2018, 24, "example")
    part1(*parse(input))
