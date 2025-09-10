import sys
from collections import deque

import parse as ps
from attrs import define

from aoc.util import timed

Instruction = tuple[str, int | str]


def parse(input: str) -> list[Instruction]:
    instructions: list[Instruction] = []

    for line in input.splitlines():
        if line == "deal into new stack":
            instruction = ("deal", "stack")
        elif incr := ps.parse("deal with increment {:d}", line):
            instruction = ("deal", *incr)
        elif cut := ps.parse("cut {:d}", line):
            instruction = ("cut", *cut)
        else:
            raise ValueError(f"Cannot parse instruction from '{line}'")

        instructions.append(instruction)

    return instructions


def perform(deck: deque[int], instruction: Instruction) -> deque[int]:
    match instruction:
        case ("deal", "stack"):
            deck.reverse()
        case ("deal", incr) if isinstance(incr, int):
            new_deck: list[int] = [-1] * len(deck)

            for idx, card in enumerate(deck):
                new_deck[(idx * incr) % len(deck)] = card

            deck = deque(new_deck)
        case ("cut", cut) if isinstance(cut, int):
            cut %= len(deck)
            deck.rotate(-cut)
        case _:
            raise ValueError(f"Invalid instruction '{instruction}'")

    return deck


def shuffle(cards: list[int], instructions: list[Instruction]):
    deck = deque(cards)

    for instruction in instructions:
        deck = perform(deck, instruction)

    return list(deck)


@define
class Transformation:
    """Class that represents an affine transformation f(x) = ax + b

    :param a: Multiplicative coefficient of the transformation
    :param b: Additive coefficient of the transformation
    """

    a: int
    b: int

    @classmethod
    def from_instructions(
        cls, instructions: list[Instruction], mod: int
    ) -> "Transformation":
        """Combine instructions by representing a a shuffle as an affine function f where
        :param instructions: Instructions to combine into the transformation
        :parm mod: Mod to take over the values of a, b to avoid going out of range
        :raises ValueError: Error when an instruction is invalid
        :return: Transformation from combining the given instructions
        """
        a, b = 1, 0

        for instruction in instructions:
            match instruction:
                case ("deal", "stack"):
                    a = -a % mod
                    b = (-b - 1) % mod

                case ("deal", incr) if isinstance(incr, int):
                    a = (a * incr) % mod
                    b = (b * incr) % mod

                case ("cut", cut) if isinstance(cut, int):
                    a = a % mod
                    b = (b - cut) % mod

                case _:
                    raise ValueError(f"Invalid instruction '{instruction}'")

        return Transformation(a, b)

    def repeat(self, n_repeats: int, mod: int) -> "Transformation":
        """Repeat the same shuffle (affine transformation) n times

        :param n_repeats: How often the transformation should be repeated
        :return: Collapsed transformation that represents the repeat
        """
        an = pow(self.a, n_repeats, mod)

        if self.a == 1:
            bn = (self.b * n_repeats) % mod
        else:
            inv = pow((self.a - 1) % mod, -1, mod)
            bn = (self.b * (an - 1) * inv) % mod

        return Transformation(an, bn)

    def get(self, x: int, mod: int) -> int:
        return (self.a * x + self.b) % mod

    def inv(self, fx: int, mod: int) -> int:
        return ((fx - self.b) * pow(self.a, -1, mod)) % mod


def part1(instructions: list[Instruction]) -> int:
    N_CARDS = 10_007

    cards = [card for card in range(N_CARDS)]
    cards = shuffle(cards, instructions)

    return cards.index(2019)


def part1_affine(instructions: list[Instruction]) -> int:
    N_CARDS = 10_007

    transformation = Transformation.from_instructions(instructions, N_CARDS)
    return transformation.get(2019, N_CARDS)


def part2(instructions: list[Instruction]) -> int:
    N_CARDS = 119_315_717_514_047
    N_SHUFFLES = 101_741_582_076_661

    transformation = Transformation.from_instructions(instructions, N_CARDS)
    transformation = transformation.repeat(N_SHUFFLES, N_CARDS)

    return transformation.inv(2020, N_CARDS)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    shuffle(list(range(10)), [("cut", 6), ("deal", 7), ("deal", "stack")])
