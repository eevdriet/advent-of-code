import sys

from aoc.util import timed


def parse(input: str) -> list[int]:
    return [int(num) for num in input.strip()]


def simulate(cups: list[int], *, n_rounds: int) -> dict[int, int]:
    # Extract particular cups
    curr_cup = cups[0]
    min_cup = min(cups)
    max_cup = max(cups)

    # Keep track of the cups as a linked list to the next element
    # This makes insertion/moving around a lot more efficient
    next_cups = dict(zip(cups, cups[1:] + cups[:1]))

    for round_ in range(n_rounds):
        # Target the three cups to move after the current
        first = next_cups[curr_cup]
        second = next_cups[first]
        third = next_cups[second]

        # Find a destination not among the three cups by continuously subtracting
        dst = curr_cup - 1

        while dst < min_cup or dst in [first, second, third]:
            dst -= 1
            if dst < min_cup:
                dst = max_cup

        # Insert three cups right after the destination cup
        next_cups[curr_cup] = next_cups[third]
        next_cups[third] = next_cups[dst]
        next_cups[dst] = first

        curr_cup = next_cups[curr_cup]

    return next_cups


def part1(cups: list[int], n_rounds: int = 100) -> str:
    next_cups = simulate(cups, n_rounds=n_rounds)

    labels = [next_cups[1]]
    while (next_cup := next_cups[labels[-1]]) != 1:
        labels.append(next_cup)

    return "".join(str(digit) for digit in labels)


def part2(cups: list[int], n_rounds: int = 10_000_000) -> int:
    max_cup = max(cups)
    extended_cups = cups + [num for num in range(max_cup + 1, 1_000_001)]
    next_cups = simulate(extended_cups, n_rounds=n_rounds)

    next1 = next_cups[1]
    next11 = next_cups[next1]

    return next1 * next11


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    part1(parse("389125467"))
