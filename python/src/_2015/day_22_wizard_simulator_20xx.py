import sys
from collections import deque
from dataclasses import dataclass, replace
from typing import Dict, Tuple

from aoc.util import timed


@dataclass(frozen=True)
class Player:
    hit_points: int
    damage: int
    armor: int

    mana: int = 0
    spent: int = 0
    effects: Dict[str, int] = None

    @classmethod
    def parse(cls, input: str) -> "Player":
        points, damage, *_ = (line.split(":")[1].strip() for line in input.splitlines())

        return Player(int(points), int(damage), 0)

    def apply_effects(self, boss_hp: int) -> Tuple["Player", int]:
        """Apply active effects to player and boss, returning new player and new boss HP."""
        new_effects = {}
        new_mana = self.mana
        new_armor = 0
        damage_to_boss = 0

        for name, timer in self.effects.items():
            if name == "Shield":
                new_armor = 7
            if name == "Poison":
                damage_to_boss += 3
            if name == "Recharge":
                new_mana += 101

            if timer > 1:
                new_effects[name] = timer - 1

        return (
            replace(self, mana=new_mana, armor=new_armor, effects=new_effects),
            boss_hp - damage_to_boss,
        )

    def can_cast(self, spell: str, cost: int) -> bool:
        return self.mana >= cost and spell not in self.effects

    def cast(self, spell: str, cost: int, boss_hp: int) -> Tuple["Player", int]:
        """Return new player and new boss HP after casting a spell."""
        new_mana = self.mana - cost
        new_spent = self.spent + cost
        new_effects = dict(self.effects)

        if spell == "Magic Missile":
            boss_hp -= 4
        elif spell == "Drain":
            boss_hp -= 2
            new_hp = self.hit_points + 2
            return (
                replace(self, hit_points=new_hp, mana=new_mana, spent=new_spent),
                boss_hp,
            )
        elif spell == "Shield":
            new_effects["Shield"] = 6
        elif spell == "Poison":
            new_effects["Poison"] = 6
        elif spell == "Recharge":
            new_effects["Recharge"] = 5

        return (
            replace(self, mana=new_mana, spent=new_spent, effects=new_effects),
            boss_hp,
        )


def min_mana_to_win(boss: Player, hard_mode=False) -> int:
    min_win = sys.maxsize

    spells = {
        "Magic Missile": 53,
        "Drain": 73,
        "Shield": 113,
        "Poison": 173,
        "Recharge": 229,
    }

    player = Player(50, 0, 0, mana=500, effects={}, spent=0)

    # (mana_spent, player, boss_hp, player_turn)
    queue = deque([(0, player, boss.hit_points, True)])

    while queue:
        spent, player, boss_hp, player_turn = queue.popleft()

        if spent >= min_win:
            continue

        # Hard mode: lose 1 HP at start of player's turn
        if hard_mode and player_turn:
            player = replace(player, hit_points=player.hit_points - 1)
            if player.hit_points <= 0:
                continue

        # Apply effects
        player, boss_hp = player.apply_effects(boss_hp)
        if boss_hp <= 0:
            min_win = min(min_win, spent)
            continue

        if player_turn:
            # Try casting each spell
            for spell, cost in spells.items():
                if player.can_cast(spell, cost):
                    new_player, new_boss_hp = player.cast(spell, cost, boss_hp)
                    queue.append((new_player.spent, new_player, new_boss_hp, False))
        else:
            # Boss turn
            damage = max(1, boss.damage - player.armor)
            new_hp = player.hit_points - damage
            if new_hp > 0:
                queue.append(
                    (player.spent, replace(player, hit_points=new_hp), boss_hp, True)
                )

    return min_win


def part1(enemy: Player) -> int:
    return min_mana_to_win(enemy, hard_mode=False)


def part2(enemy: Player) -> int:
    return min_mana_to_win(enemy, hard_mode=True)


if __name__ == "__main__":
    input = sys.stdin.read()
    boss = Player.parse(input)

    result1, elapsed = timed(part1, boss)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, boss)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
