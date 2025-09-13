import sys

from attrs import define

from aoc.util import timed


def parse(input: str) -> tuple[int, int]:
    line1, line2 = input.splitlines()
    return int(line1), int(line2)


MOD = 20201227


@define
class ComboBreaker:
    card: int
    door: int

    def break_combo(self, key: int, subject: int = 7) -> int:
        val = 1
        loop_size = 0

        while val != key:
            val = (val * subject) % MOD
            loop_size += 1

        return pow(self.door, loop_size, MOD)


def part1(card: int, door: int) -> int:
    breaker = ComboBreaker(card, door)
    return breaker.break_combo(card)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, *parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
