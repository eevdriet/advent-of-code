import sys

import parse as ps
from attrs import define

from aoc.util import timed


@define
class Password:
    password: str

    letter: str
    low: int
    high: int

    @classmethod
    def parse(cls, text: str) -> "Password":
        min_count, max_count, letter, password = ps.parse("{:d}-{:d} {}: {}", text)
        return cls(password, letter, min_count, max_count)

    def is_valid(self, *, part: int) -> bool:
        if part == 1:
            return self.password.count(self.letter) in range(self.low, self.high + 1)

        if part == 2:
            has_low = (
                self.low in range(1, len(self.password) + 1)
                and self.password[self.low - 1] == self.letter
            )
            has_high = (
                self.high in range(1, len(self.password) + 1)
                and self.password[self.high - 1] == self.letter
            )

            return has_low ^ has_high

        raise ValueError(f"Invalid part {part} given")


def parse(input: str) -> list[Password]:
    return [Password.parse(line) for line in input.splitlines()]


def part1(passwords: list[Password]) -> int:
    return sum(1 for password in passwords if password.is_valid(part=1))


def part2(passwords: list[Password]) -> int:
    return sum(1 for password in passwords if password.is_valid(part=2))


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
