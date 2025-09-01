import heapq
import re
import sys
from collections import defaultdict, deque
from copy import deepcopy
from enum import IntEnum
from itertools import combinations
from typing import Generator

from aoc.io import open_file
from aoc.util import combinations_xy, timed

Element = str


class ItemType(IntEnum):
    MICROCHIP = 0
    GENERATOR = 1


class Item:
    def __init__(self, elem: Element, typ: ItemType):
        self.elem = elem
        self.typ = typ

    def __repr__(self) -> str:
        suffix = "G" if self.typ == ItemType.GENERATOR else "M"
        return f"{self.elem}{suffix}"

    def __hash__(self):
        return hash((self.elem, self.typ))


class Floor:
    def __init__(self, items: set[Item]):
        self.items = items

    def is_valid(self) -> bool:
        # Only microchips is always valid
        if all(item.typ == ItemType.MICROCHIP for item in self.items):
            return True

        # Otherwise, every microchip should have an associated generator
        chips = (item for item in self.items if item.typ == ItemType.MICROCHIP)

        for chip in chips:
            generator = Item(chip.elem, ItemType.GENERATOR)

            if not generator in self.items:
                return False

        return True

    def __repr__(self) -> str:
        items = sorted([str(item) for item in self.items])
        repr = ", ".join(items)
        return f"[{repr}]"


class State:
    def __init__(self, floors: list[Floor], elevator: int = 0):
        assert 0 <= elevator < len(floors)

        self.floors = floors
        self.elevator = elevator

    def is_complete(self):
        # Single floor is always valid
        if len(self.floors) <= 1:
            return True

        # Otherwise, all items should be on the top floor
        *floors, _top_floor = self.floors
        return all(not floor.items for floor in floors)

    @property
    def top_level(self) -> int:
        return len(self.floors) - 1

    @property
    def bottom_level(self) -> int:
        for level in range(self.top_level):
            floor = self.floors[level]
            if floor.items:
                return level

        return self.top_level

    def copy(self) -> "State":
        floors = deepcopy(self.floors)
        return State(floors, elevator=self.elevator)

    def generate_next(self) -> Generator["State", None, None]:
        level = self.elevator
        floor = self.floors[level]

        # Try to go up or down if possible
        for dir in [1, -1]:
            # Verify we go to a valid (and practical) level
            next_level = level + dir
            if not (self.bottom_level <= next_level <= self.top_level):
                continue

            # Try all items that can be moved
            next_floor = self.floors[next_level]

            for items in combinations_xy(floor.items, range(1, 3)):
                # Move items from the current floor to the next
                items = set(items)

                floor.items -= items
                self.elevator += dir
                next_floor.items |= items

                # Generate the next state and backtrack afterwards
                yield self.copy()

                next_floor.items -= items
                self.elevator -= dir
                floor.items |= items

    def __repr__(self):
        floors = []

        for level, floor in enumerate(self.floors):
            prefix = f"({level})" if level == self.elevator else str(level)
            floors.append(f"{prefix} {floor}")

        return " - ".join(floors)

    def __hash__(self):
        # Determine on which floor each item is, first chips then generators
        item_floors: dict[Element, list[int]] = defaultdict(lambda: [-1, -1])

        for level, floor in enumerate(self.floors):
            for item in floor.items:
                item_floors[item.elem][item.typ] = level

        floors = str(sorted(item_floors.values()))
        return hash((self.elevator, floors))


def parse(input: str) -> State:
    """
    The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
    The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
    The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.
    The fourth floor contains nothing relevant.
    """
    floors = []

    for line in input.splitlines():
        items = set()

        for elem in re.findall(r"(\w+)-compatible microchip", line):
            items.add(Item(elem[0].upper() + elem[1], ItemType.MICROCHIP))
        for elem in re.findall(r"(\w+) generator", line):
            items.add(Item(elem[0].upper() + elem[1], ItemType.GENERATOR))

        floors.append(Floor(items))

    return State(floors)


def find_min_steps(initial: State) -> int:
    queue = deque([(initial, 0)])
    seen = set()

    while queue:
        # Verify whether the current state gives the solution
        state, n_steps = queue.popleft()
        if state.is_complete():
            return n_steps

        # Otherwise, try all other states
        for next_state in state.generate_next():
            if next_state not in seen:
                queue.append((next_state, n_steps + 1))
            else:
                pass

    # Couldn't reach final state
    return -1


def part1(state: State) -> int:
    return find_min_steps(state)


def part2(state: State) -> int:
    next_state = state.copy()
    new_items = {
        Item("elerium", ItemType.GENERATOR),
        Item("elerium", ItemType.MICROCHIP),
        Item("dilithium", ItemType.GENERATOR),
        Item("dilithium", ItemType.MICROCHIP),
    }

    next_state.floors[0].items |= new_items
    return find_min_steps(next_state)


if __name__ == "__main__":
    # input = sys.stdin.read()
    # state = parse(input)
    #
    # result1, elapsed = timed(part1, state)
    # print(f"Part 1: {result1} ({elapsed} elapsed)")
    #
    # result2, elapsed = timed(part2, state)
    # print(f"Part 2: {result2} ({elapsed} elapsed)")

    with open_file(2016, 11) as file:
        state = parse(file.read())
        part1(state)
