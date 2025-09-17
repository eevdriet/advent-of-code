import re
import sys
from collections import defaultdict
from enum import StrEnum
from math import prod

from attrs import define

from aoc.io import read_file
from aoc.util import timed
from aoc.util.re import find_num


class Mineral(StrEnum):
    ORE = "ore"
    GEODE = "geode"
    CLAY = "clay"
    OBSIDIAN = "obsidian"


@define
class Blueprint:
    id: int
    # robot_costs[Mineral][Mineral] = amount
    robot_costs: dict[Mineral, dict[Mineral, int]]

    def find_max_target(self, n_minutes: int) -> int:
        # Precompute optimistic bound (triangular numbers)
        tri = [(t - 1) * t // 2 for t in range(n_minutes + 1)]

        max_geodes = 0

        # Caps: we never need more robots than the max cost of their resource
        max_ore = max(costs.get(Mineral.ORE, 0) for costs in self.robot_costs.values())
        max_clay = self.robot_costs.get(Mineral.OBSIDIAN, {}).get(Mineral.CLAY, 0)
        max_obsidian = self.robot_costs.get(Mineral.GEODE, {}).get(Mineral.OBSIDIAN, 0)

        def dfs(
            t: int,
            goal: Mineral,
            robots: dict[Mineral, int],
            minerals: dict[Mineral, int],
        ):
            nonlocal max_geodes

            geodes = minerals.get(Mineral.GEODE, 0)
            if (
                # Pruning
                goal == Mineral.ORE
                and robots[Mineral.ORE] >= max_ore
                or goal == Mineral.CLAY
                and robots[Mineral.CLAY] >= max_clay
                or goal == Mineral.OBSIDIAN
                and (
                    robots[Mineral.OBSIDIAN] >= max_obsidian
                    or robots[Mineral.CLAY] == 0
                )
                or goal == Mineral.GEODE
                and robots[Mineral.OBSIDIAN] == 0
                or geodes + robots[Mineral.GEODE] * t + tri[t] <= max_geodes
            ):
                return

            while t:
                costs = self.robot_costs.get(goal, {})
                if all(minerals[m] >= c for m, c in costs.items()):
                    # Build robot of type `goal`
                    new_robots = robots.copy()
                    new_robots[goal] += 1

                    new_minerals = minerals.copy()
                    for m in Mineral:
                        new_minerals[m] += robots[m] - costs.get(m, 0)

                    # Try all possible new goals
                    for g in Mineral:
                        dfs(t - 1, g, new_robots, new_minerals)
                    return

                # Otherwise, wait 1 step
                minerals = minerals.copy()
                for m in Mineral:
                    minerals[m] += robots[m]
                t -= 1

            # Out of time
            max_geodes = max(max_geodes, minerals[Mineral.GEODE])

        # Start with 1 ore robot
        start_robots = defaultdict(int, {Mineral.ORE: 1})
        start_minerals = defaultdict(int)

        for g in Mineral:
            dfs(n_minutes, g, start_robots, start_minerals)

        return max_geodes


def parse(input: str) -> list[Blueprint]:
    """
    Blueprint 1:
      Each ore robot costs 4 ore.
      Each clay robot costs 2 ore.
      Each obsidian robot costs 3 ore and 14 clay.
      Each geode robot costs 2 ore and 7 obsidian.
    """
    blueprints = []

    for line in input.strip().splitlines():
        id_line, cost_lines = line.split(":")
        id = find_num(id_line)

        costs: dict[Mineral, dict[Mineral, int]] = {}

        for line in cost_lines.split(". "):
            mineral_match = re.match(r"Each (\w+) robot costs ", line.strip())
            mineral = Mineral(mineral_match.group(1))

            cost = defaultdict(int)
            for cost_match in re.finditer(r"(\d+) (\w+)", line[mineral_match.end() :]):
                amount, cost_mineral = cost_match.groups()
                cost[Mineral(cost_mineral)] = int(amount)

            costs[mineral] = cost

        blueprint = Blueprint(id, costs)
        blueprints.append(blueprint)

    return blueprints


def part1(blueprints: list[Blueprint]) -> int:
    n_minutes = 24

    return sum(
        blueprint.id * blueprint.find_max_target(n_minutes) for blueprint in blueprints
    )


def part2(blueprints: list[Blueprint]) -> int:
    n_minutes = 32

    return prod(blueprint.find_max_target(n_minutes) for blueprint in blueprints[:3])


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2022, 19, "example")
    part1(parse(input))
