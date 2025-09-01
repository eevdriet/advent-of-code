import re
import sys
from collections import defaultdict

from attrs import define

from aoc.io import open_file
from aoc.util import combinations_xy, timed


@define
class Item:
    name: str
    cost: int
    damage: int
    armor: int

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)


@define
class Player:
    hit_points: int
    damage: int
    armor: int

    items: set[Item] = set()

    @classmethod
    def parse(cls, input: str) -> "Player":
        points, damage, armor, *_ = (
            line.split(":")[1].strip() for line in input.splitlines()
        )

        return Player(int(points), int(damage), int(armor))

    @property
    def cost(self):
        return sum(item.cost for item in self.items)

    def turns_to_defeat(self, other: "Player"):
        damage = max(1, self.damage - other.armor)

        return (other.hit_points + damage - 1) // damage

    def can_defeat(self, other: "Player"):
        us = self.turns_to_defeat(other)
        them = other.turns_to_defeat(self)

        return us <= them

    def equip(self, *items: Item):
        for item in items:
            self.damage += item.damage
            self.armor += item.armor

            self.items.add(item)

    def drop(self, *items: Item):
        for item in items:
            self.damage -= item.damage
            self.armor -= item.armor

            self.items.discard(item)


Shop = dict[str, list[Item]]


def parse_shop() -> Shop:
    with open_file(2015, 21, name="shop") as file:
        input = file.read()

    shop = defaultdict(list)

    for section in input.split("\n\n"):
        header, *lines = section.splitlines()
        header = header.split(":")[0]

        # Skip section header
        for line in lines:
            name, cost, damage, armor, *_ = re.split(r" {2,}", line)

            item = Item(name, int(cost), int(damage), int(armor))
            shop[header].append(item)

    return shop


shop = parse_shop()
player = Player(100, 0, 0)


def simulate(enemy: Player) -> tuple[int, int]:
    min_cost_to_win = sys.maxsize
    max_cost_to_lose = 0

    for weapon in shop["Weapons"]:
        for armor in combinations_xy(shop["Armor"], range(2)):
            for rings in combinations_xy(shop["Rings"], range(3)):
                items = (weapon, *armor, *rings)
                player.equip(*items)

                if player.can_defeat(enemy):
                    min_cost_to_win = min(player.cost, min_cost_to_win)
                else:
                    max_cost_to_lose = max(player.cost, max_cost_to_lose)

                player.drop(*items)

    return min_cost_to_win, max_cost_to_lose


def part1(enemy: Player) -> int:
    min_cost, _ = simulate(enemy)

    return min_cost


def part2(enemy: Player) -> int:
    _, max_cost = simulate(enemy)

    return max_cost


if __name__ == "__main__":
    input = sys.stdin.read()
    boss = Player.parse(input)

    result1, elapsed = timed(part1, boss)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, boss)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
