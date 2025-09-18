import sys

from attrs import define

from aoc.util import timed

_NUM_DIGITS: dict[int, str] = {0: "0", 1: "1", 2: "2", -1: "-", -2: "="}


def snafu(num: int) -> str:
    carry = 0
    digits = []

    while num or carry:
        num, digit = divmod(num, 5)

        if digit <= 2:
            digits.append(str(digit))
        else:
            digits.append({-1: "-", -2: "="}[digit - 5])
            digits.append("1")

    return "".join(reversed(digits))


@define
class Snafu:
    digits: str

    @classmethod
    def from_base10(cls, num: int) -> "Snafu":
        digits = []

        while num:
            num, digit = divmod(num, 5)

            if digit <= 2:
                digits.append(str(digit))
            else:
                digits.append({-1: "-", -2: "="}[digit - 5])
                num += 1

        return cls("".join(reversed(digits)))

    _DIGIT_NUMS: dict[str, int] = {"0": 0, "1": 1, "2": 2, "-": -1, "=": -2}
    _NUM_DIGITS: dict[int, str] = {0: "0", 1: "1", 2: "2", -1: "-", -2: "="}

    def base10(self) -> int:
        return sum(
            self._DIGIT_NUMS[digit] * (5**power)
            for power, digit in enumerate(reversed(self.digits))
        )


def parse(input: str) -> list[Snafu]:
    return [Snafu(line) for line in input.splitlines()]


def part1(nums: list[Snafu]) -> str:
    snafu_sum = sum(num.base10() for num in nums)
    sum_snafu = Snafu.from_base10(snafu_sum)

    return sum_snafu.digits


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
