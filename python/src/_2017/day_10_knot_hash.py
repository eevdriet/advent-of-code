import operator
import sys
from functools import reduce

from aoc.util import timed


def parse(input: str) -> str:
    return input.strip()


def tie_knots(lengths: list[int], size: int, *, n_rounds: int = 1) -> str:
    nums = list(range(size))
    pos = 0
    skip = 0

    for _ in range(n_rounds):
        for length in lengths:
            # Reverse segment of length from position
            left = pos
            right = pos + length - 1

            while left < right:
                l = left % len(nums)
                r = right % len(nums)

                nums[l], nums[r] = nums[r], nums[l]
                left += 1
                right -= 1

            # Move forward and increase skip size
            pos = (pos + length + skip) % len(nums)
            skip += 1

    # For the first part, just find product of the first two numbers
    if n_rounds == 1:
        return str(nums[0] * nums[1])

    # Otherwise find the dense hash from the XOR of all 16-blocks
    step = 16
    blocks = [nums[idx : idx + step] for idx in range(0, size, step)]
    hashes = [reduce(operator.xor, block) for block in blocks]

    return "".join((f"{hash:02x}" for hash in hashes))


def part1(input: str) -> str:
    lengths = [int(num) for num in input.split(",")]
    return tie_knots(lengths, 256)


def part2(input: str) -> str:
    codes = [ord(ch) for ch in input.strip()]
    codes += [17, 31, 73, 47, 23]

    return tie_knots(codes, 256, n_rounds=64)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
