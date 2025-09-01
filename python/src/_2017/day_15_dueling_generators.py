import re
import sys
from typing import Generator

from aoc.util import timed

IntGen = Generator[int, None, None]


def parse(input: str) -> list[int]:
    return [int(num) for num in re.findall(r"(\d+)", input.strip())]


def create_generator(seed: int, factor: int, multiple_of: int = 1):
    MOD = 2147483647
    num = seed

    while True:
        num = (num % MOD) * (factor % MOD) % MOD

        if num % multiple_of == 0:
            yield num


def compare_generators(a: IntGen, b: IntGen, n_iters: int) -> int:
    n_matches = 0
    MASK = (1 << 16) - 1

    for _ in range(n_iters):
        # Generate next number pair
        num_a = next(a)
        num_b = next(b)

        # Verify whether the last 16 bits match
        if num_a & MASK == num_b & MASK:
            n_matches += 1

    return n_matches


def part1(starts: list[int]) -> int:
    start_a, start_b, *_ = starts

    a = create_generator(start_a, 16807)
    b = create_generator(start_b, 48271)

    return compare_generators(a, b, 40_000_000)


def part2(starts: list[int]) -> int:
    start_a, start_b, *_ = starts

    a = create_generator(start_a, 16807, 4)
    b = create_generator(start_b, 48271, 8)

    return compare_generators(a, b, 5_000_000)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    part1([65, 8921])
