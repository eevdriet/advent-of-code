import re
import sys
from collections import deque
from math import lcm
from typing import Callable, override

from attrs import define

from aoc.io import read_file
from aoc.util import timed


@define(hash=False)
class Monkey:
    id: int
    items: deque[int]
    op: Callable[[int], int]

    div: int

    true_monkey: int
    false_monkey: int

    @override
    def __hash__(self) -> int:
        return hash(self.id)


def parse(input: str) -> list[Monkey]:
    monkeys = []

    def find_nums(line: str) -> list[int]:
        return list(map(int, re.findall(r"(\d+)", line)))

    for block in input.split("\n\n"):
        lines = block.splitlines()

        assert len(lines) == 6
        id_line, items_line, op_line, test_line, true_line, false_line = lines

        # Directly number(s) from lines
        id = find_nums(id_line)[0]
        items = deque(find_nums(items_line))
        true_monkey = find_nums(true_line)[0]
        false_monkey = find_nums(false_line)[0]

        # Create divisibility test
        test_div = find_nums(test_line)[0]

        # Literally parse the operation to perform
        rhs = op_line[op_line.index("=") + 1 :]
        op = eval(f"lambda old: {rhs}")

        monkey = Monkey(id, items, op, test_div, true_monkey, false_monkey)
        monkeys.append(monkey)

    return monkeys


def monkey_business(monkeys: list[Monkey], *, part: int, n_rounds: int) -> int:
    monkey_inspections = [0] * len(monkeys)
    mod = lcm(*(monkey.div for monkey in monkeys))

    for _ in range(n_rounds):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.popleft()
                monkey_inspections[monkey.id] += 1

                worry = monkey.op(item)
                if part == 1:
                    worry //= 3
                elif part == 2:
                    worry %= mod

                # Throw the worry level to the next monkey
                throw_monkey = (
                    monkey.true_monkey
                    if worry % monkey.div == 0
                    else monkey.false_monkey
                )
                monkeys[throw_monkey].items.append(worry)

    # Multiply the counts of the 2 monkeys that inspected the most
    monkey_inspections.sort()

    return monkey_inspections[-1] * monkey_inspections[-2]


def part1(monkeys: list[Monkey]) -> int:
    return monkey_business(monkeys, part=1, n_rounds=20)


def part2(monkeys: list[Monkey]) -> int:
    return monkey_business(monkeys, part=2, n_rounds=10_000)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    example = read_file(2022, 11, "example")
    part1(parse(example))
