import ast
import sys
from copy import deepcopy
from itertools import combinations
from typing import Literal, override

from attrs import define, field

from aoc.util import timed


@define(repr=False)
class Snailfish:
    left: "Snailfish | int"
    right: "Snailfish | int"
    parent: "Snailfish | None" = field(default=None)

    def __attrs_post_init__(self):
        if isinstance(self.left, Snailfish):
            self.left.parent = self
        if isinstance(self.right, Snailfish):
            self.right.parent = self

    @classmethod
    def from_list(cls, li: list, parent: "Snailfish | None" = None) -> "Snailfish":
        left, right = li

        if isinstance(left, list):
            left = cls.from_list(left)
        if isinstance(right, list):
            right = cls.from_list(right)

        snailfish = cls(left, right, parent)

        return snailfish

    @classmethod
    def from_text(cls, text: str) -> "Snailfish":
        li = ast.literal_eval(text)
        return cls.from_list(li)

    @override
    def __repr__(self):
        return f"[{self.left!r},{self.right!r}]"

    def __add__(self, other: "Snailfish") -> "Snailfish":
        result = Snailfish(self, other)
        result.reduce()

        return result

    def __radd__(self, other: "Snailfish | Literal[0]") -> "Snailfish":
        if other == 0:
            return self

        return self.__add__(other)

    @property
    def magnitude(self) -> int:
        left = self.left.magnitude if isinstance(self.left, Snailfish) else self.left
        right = (
            self.right.magnitude if isinstance(self.right, Snailfish) else self.right
        )

        return 3 * left + 2 * right

    def reduce(self):
        while self.explode() or self.split():
            pass

    def explode(self, depth: int = 0) -> bool:
        # Verify conditions to explode and do so
        if depth >= 4 and isinstance(self.left, int) and isinstance(self.right, int):
            self._add_to_nearest_left(self.left)
            self._add_to_nearest_right(self.right)

            # Replace the exploded snailfish with 0
            if self.parent:
                if self.parent.left is self:
                    self.parent.left = 0
                else:
                    self.parent.right = 0

            return True

        # If we cannot yet explode, try to explode further down the Snailfish tree
        if isinstance(self.left, Snailfish) and self.left.explode(depth + 1):
            return True
        if isinstance(self.right, Snailfish) and self.right.explode(depth + 1):
            return True

        return False

    def split(self) -> bool:
        # If the fish is integer and >= 10, it is split into a new snailfish
        if isinstance(self.left, int):
            if self.left >= 10:
                left = self.left // 2
                right = (self.left + 1) // 2

                self.left = Snailfish(left, right, self)
                return True

        # Otherwise, continue with children of the current fish
        elif self.left.split():
            return True

        # Repeat for the other child
        if isinstance(self.right, int):
            if self.right >= 10:
                left = self.right // 2
                right = (self.right + 1) // 2

                self.right = Snailfish(left, right, self)
                return True
        elif self.right.split():
            return True

        return False

    def _add_to_nearest_left(self, val: int):
        # Find the first candidate where left can be added to
        node = self
        parent = self.parent

        while parent and parent.left is node:
            node, parent = parent, parent.parent

        # Not possible to add the value if we've reached passed the root
        if not parent:
            return

        # Find the nearest snailfish, which is the rightmost Snailfish from the parent
        target = parent.left
        while isinstance(target, Snailfish):
            target = target.right

        # If the target is already nearest, add the value
        if parent.left == target:
            parent.left += val
            return

        # Otherwise, keep going right until an integer Snailfish is found
        ref = parent.left

        while isinstance(ref, Snailfish):
            if isinstance(ref.right, int):
                ref.right += val
                return

            ref = ref.right

    def _add_to_nearest_right(self, val: int):
        # Find the first candidate where right can be added to
        node = self
        parent = self.parent

        while parent and parent.right is node:
            node, parent = parent, parent.parent

        # Not possible to add the value if we've reached passed the root
        if not parent:
            return

        # Find the nearest snailfish, which is the leftmost Snailfish from the parent
        target = parent.right
        while isinstance(target, Snailfish):
            target = target.left

        # If the target is already nearest, add the value
        if parent.right == target:
            parent.right += val
            return

        # Otherwise, keep going left until an integer Snailfish is found
        ref = parent.right

        while isinstance(ref, Snailfish):
            if isinstance(ref.left, int):
                ref.left += val
                return

            ref = ref.left


def parse(input: str) -> list[Snailfish]:
    return [Snailfish.from_text(line) for line in input.splitlines()]


def part1(snailfishes: list[Snailfish]) -> int:
    snailfish = sum(snailfishes)

    return snailfish.magnitude


def part2(snailfishes: list[Snailfish]) -> int:
    max_magnitude = 0

    for fish1, fish2 in combinations(snailfishes, r=2):
        for left, right in [(fish1, fish2), (fish2, fish1)]:
            result = deepcopy(left) + deepcopy(right)

            if result.magnitude > max_magnitude:
                max_magnitude = result.magnitude

    return max_magnitude


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    Snailfish.parse("[[[[1,2],[3,4]],[[5,6],[7,8]]],9]")
