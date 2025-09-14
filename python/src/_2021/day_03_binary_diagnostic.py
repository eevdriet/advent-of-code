import sys
from math import log2

from aoc.util import timed


def parse(input: str) -> list[int]:
    return [int(num, 2) for num in input.splitlines()]


def part1(nums: list[int]) -> int:
    gamma, epsilon = 0, 0
    bit = 1

    while True:
        # Verify how many 1-bits are set; if none are set, stop producing gamma
        n_bits_set = sum(bool(num & bit) for num in nums)
        if n_bits_set == 0:
            break

        # Set gamma if 1 is most common, otherwise set epislon
        if n_bits_set > len(nums) // 2:
            gamma |= bit
        else:
            epsilon |= bit

        bit <<= 1

    return gamma * epsilon


def part2(nums: list[int]) -> int:
    n_bits = 1 + int(log2(max(nums)))

    def diagnose(choose_common: bool) -> int:
        candidates = set(nums)
        bit = 1 << (n_bits - 1)

        for idx in range(n_bits - 1, -1, -1):  # from MSB to LSB
            # Choose any left-over candidate
            if len(candidates) == 1:
                break

            # Check how many bits are set and whether to keep the most set bit
            n_bits_set = sum(bool(num & bit) for num in candidates)
            n_bits_unset = len(candidates) - n_bits_set

            keep_bit = (
                n_bits_set >= n_bits_unset
                if choose_common
                else n_bits_set < n_bits_unset
            )

            # Weed out invalid candidates and move on to the next bit
            candidates = {
                num for num in candidates if bool(num & bit) == bool(keep_bit)
            }

            bit >>= 1

        assert len(candidates) == 1
        return next(iter(candidates))

    oxygen = diagnose(choose_common=True)
    co2 = diagnose(choose_common=False)

    return oxygen * co2


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
