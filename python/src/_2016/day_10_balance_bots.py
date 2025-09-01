import sys
from collections import defaultdict
from dataclasses import dataclass
from math import prod
from typing import Optional

import parse as ps

from aoc.util import timed


@dataclass
class Instruction:
    pass


@dataclass
class Give(Instruction):
    bot: int
    chip: int


@dataclass
class Distribute(Instruction):
    bot: int

    low_type: str
    low_id: int

    high_type: str
    high_id: int


def parse(input: str) -> list[Instruction]:
    instructions = []

    for line in input.splitlines():
        if r := ps.parse("value {val:d} goes to bot {bot:d}", line):
            instructions.append(Give(r["bot"], r["val"]))
        elif r := ps.parse(
            "bot {bot:d} gives low to {low_type:w} {low_id:d} and high to {high_type:w} {high_id:d}",
            line,
        ):
            instructions.append(
                Distribute(
                    r["bot"], r["low_type"], r["low_id"], r["high_type"], r["high_id"]
                )
            )

    return instructions


def assign_chips(
    instructions: list[Instruction],
    *,
    end_chips: Optional[tuple[int, int]] = None,
) -> int:
    bots = defaultdict(list)
    outputs = defaultdict(list)
    gives: dict[int, Distribute] = {}

    def gives_to(chip: int, typ: str, id: int):
        match typ:
            case "bot":
                bots[id].append(chip)
            case "output":
                outputs[id].append(chip)

    for instruction in instructions:
        match instruction:
            # Give the bot a new chip
            case Give(bot, chip):
                bots[bot].append(chip)

            # Otherwise, remember how each bot distributes its chips
            case Distribute(bot) as give:
                gives[bot] = give

    while bots:
        for bot, chips in dict(bots).items():
            # Only distribute chips where possible
            if len(chips) != 2:
                continue

            # Determine whether this bot sorts the requested chips
            low, high = sorted(bots.pop(bot))
            if end_chips is not None and [low, high] == sorted(end_chips):
                return bot

            # Otherwise, give to the other bots
            give = gives[bot]
            gives_to(low, give.low_type, give.low_id)
            gives_to(high, give.high_type, give.high_id)

    return prod(outputs[id][0] for id in range(3))


def part1(instructions: list[Instruction]) -> int:
    return assign_chips(instructions, end_chips=(17, 61))


def part2(instructions: list[Instruction]) -> int:
    return assign_chips(instructions)


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
