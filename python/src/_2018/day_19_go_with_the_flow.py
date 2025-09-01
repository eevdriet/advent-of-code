import re
import sys
from collections import defaultdict

import parse as ps

from _2018.day_16_chronal_classification import OPS, Registers
from aoc.io import read_file
from aoc.util import timed

Op = tuple[str, list[int]]


def parse(input: str) -> tuple[list[Op], int]:
    first_line, *lines = input.splitlines()

    ip_idx, *_ = ps.parse("#ip {:d}", first_line)

    ops = []
    for line in lines:
        code, *val_strs = line.split(" ")
        vals = [int(num) for num in val_strs]

        ops.append((code, vals))

    return ops, ip_idx


def part1(ops: list[Op], ip_idx: int) -> int:
    regs: Registers = [0] * 6

    while True:
        ip = regs[ip_idx]

        code, vals = ops[ip]
        op = OPS[code]
        op(regs, *vals)

        new_ip = regs[ip_idx] + 1
        if not new_ip in range(len(ops)):
            break

        regs[ip_idx] += 1

    return regs[0]


def part2(ops: list[Op], ip_idx: int) -> int:
    a = 11
    b = 5
    number_to_factorize = 10551236 + a * 22 + b

    factors = defaultdict(lambda: 0)
    possible_prime_divisor = 2
    while possible_prime_divisor**2 <= number_to_factorize:
        while number_to_factorize % possible_prime_divisor == 0:
            number_to_factorize /= possible_prime_divisor
            factors[possible_prime_divisor] += 1
        possible_prime_divisor += 1
    if number_to_factorize > 1:
        factors[number_to_factorize] += 1

    sum_of_divisors = 1
    for prime_factor in factors:
        sum_of_divisors *= (prime_factor ** (factors[prime_factor] + 1) - 1) / (
            prime_factor - 1
        )

    return sum_of_divisors


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, *parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2018, 19).splitlines()
    a, b = map(int, [re.findall(r"\d+", input[i])[1] for i in [22, 24]])
    number_to_factorize = 10551236 + a * 22 + b

    factors = defaultdict(lambda: 0)
    possible_prime_divisor = 2

    while possible_prime_divisor**2 <= number_to_factorize:
        while number_to_factorize % possible_prime_divisor == 0:
            number_to_factorize /= possible_prime_divisor
            factors[possible_prime_divisor] += 1
        possible_prime_divisor += 1

    if number_to_factorize > 1:
        factors[number_to_factorize] += 1

    sum_of_divisors = 1
    for prime_factor in factors:
        sum_of_divisors *= (prime_factor ** (factors[prime_factor] + 1) - 1) / (
            prime_factor - 1
        )

    print(sum_of_divisors)
