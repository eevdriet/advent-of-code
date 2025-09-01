import sys
from collections import deque
from typing import Optional

from attrs import define, field

from aoc.util import timed

Coord = tuple[int, int]


@define(hash=True)
class Player:
    id: str = field(hash=False)
    x: int = field(hash=False)
    y: int = field(hash=False)
    hp: int = field(default=200, hash=False)

    @property
    def pos(self) -> Coord:
        return self.x, self.y

    @pos.setter
    def pos(self, pos: Coord):
        self.x, self.y = pos

    def dist(self, other: "Player") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def move(self, enemies: set["Player"], open_area: set[Coord], occupied: set[Coord]):
        if any(self.dist(enemy) == 1 for enemy in enemies):
            return

        # All squares adjacent to enemies that are free
        targets = {
            pos
            for enemy in enemies
            for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]
            if (pos := (enemy.x + dx, enemy.y + dy)) in open_area
            and pos not in occupied
        }
        if not targets:
            return

        # Determine which step to take via BFS
        next_pos = self.step(targets, (open_area - occupied) | {self.pos})
        if next_pos:
            self.pos = next_pos

    def step(self, targets: set[Coord], free: set[Coord]) -> Optional[Coord]:
        start = self.pos
        queue = deque([(start, 0)])
        seen = {start}
        parents: dict[Coord, Optional[Coord]] = {start: None}
        found = []
        min_dist = None

        while queue:
            coord, dist = queue.popleft()

            if min_dist is not None and dist > min_dist:
                break  # we already found the closest distance

            if coord in targets:
                min_dist = dist
                found.append(coord)
                continue

            for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                nx, ny = coord[0] + dx, coord[1] + dy
                nxt = (nx, ny)
                if nxt in free and nxt not in seen:
                    seen.add(nxt)
                    parents[nxt] = coord
                    queue.append((nxt, dist + 1))

        if not found:
            return None

        # Choose target in reading order
        target = min(found, key=lambda c: (c[1], c[0]))

        # Backtrack to find first step from start
        cur = target
        while parents[cur] != start:
            cur = parents[cur]
        return cur

    def attack(self, enemies: set["Player"]):
        # Adjacent enemies
        adjacent = [
            enemy for enemy in enemies if self.dist(enemy) == 1 and enemy.hp > 0
        ]
        enemy = min(adjacent, key=lambda e: (e.hp, e.y, e.x), default=None)
        if enemy is not None:
            enemy.hp -= 3


@define
class Game:
    elves: set[Player]
    goblins: set[Player]
    area: set[Coord]

    def score(self, n_rounds: int) -> int:
        return n_rounds * (
            sum(elf.hp for elf in self.elves) + sum(g.hp for g in self.goblins)
        )

    def play(self, max_rounds: Optional[int] = None) -> int:
        n_rounds = 0

        while (
            self.elves
            and self.goblins
            and (max_rounds is None or n_rounds < max_rounds)
        ):
            players = sorted(self.elves | self.goblins, key=lambda p: (p.y, p.x))

            for player in players:
                if player.hp <= 0:
                    continue

                enemies = self.goblins if player.id.startswith("E") else self.elves
                if not enemies:
                    # combat ends before round is complete -> don’t count this round
                    return self.score(n_rounds)

                occupied = {
                    p.pos
                    for p in self.elves | self.goblins
                    if p.hp > 0 and p is not player
                }

                player.move(enemies, self.area, occupied)
                player.attack(enemies)

            # End of round: remove dead units and increment round count
            self.elves = {elf for elf in self.elves if elf.hp > 0}
            self.goblins = {g for g in self.goblins if g.hp > 0}
            n_rounds += 1

        return self.score(n_rounds)


def parse(input: str) -> Game:
    elves = set()
    goblins = set()
    open_area = set()

    for y, row in enumerate(input.splitlines()):
        for x, cell in enumerate(row):
            if cell != "#":
                open_area.add((x, y))

            match cell:
                case "E":
                    elves.add(Player(f"E{len(elves)}", x, y))
                case "G":
                    goblins.add(Player(f"G{len(goblins)}", x, y))

    return Game(elves, goblins, open_area)


def part1(game: Game) -> int:
    return game.play()


def part2(game: Game) -> int:
    return 0


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
