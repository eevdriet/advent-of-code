import sys
from copy import deepcopy
from operator import eq, gt, lt

import parse as ps

from aoc.util import timed

Aunt = dict[str, int]
Tape = dict[str, int]

GIFT_TAPE: Tape = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def parse(input: str) -> list[Aunt]:
    def parse_aunt(line: str) -> Aunt:
        num, properties = ps.parse("Sue {:d}: {}", line)

        aunt = {}
        aunt["num"] = num

        for prop_str in properties.split(", "):
            prop, val = prop_str.split(": ")
            aunt[prop] = int(val)

        return aunt

    return [parse_aunt(line) for line in input.splitlines()]


def part1(aunts: list[Aunt]) -> int:
    search_aunts = deepcopy(aunts)

    for prop, val in GIFT_TAPE.items():
        search_aunts = [
            aunt for aunt in search_aunts if prop not in aunt or aunt[prop] == val
        ]

    assert len(search_aunts) == 1
    return search_aunts[0]["num"]


def part2(aunts: list[Aunt]) -> int:
    search_aunts = deepcopy(aunts)
    OPS = {"cats": gt, "trees": gt, "pomeranians": lt, "goldfish": lt}

    for prop, val in GIFT_TAPE.items():
        op = OPS.get(prop, eq)
        search_aunts = [
            aunt for aunt in search_aunts if prop not in aunt or op(aunt[prop], val)
        ]

    assert len(search_aunts) == 1
    return search_aunts[0]["num"]


if __name__ == "__main__":
    input = sys.stdin.read()
    aunts = parse(input)

    result1, elapsed = timed(part1, aunts)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, aunts)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
