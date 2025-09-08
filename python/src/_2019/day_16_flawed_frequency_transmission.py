import sys

from aoc.util import timed


def parse(input: str) -> str:
    return input.strip()


def fft(n: str, n_phases: int, debug: bool = False) -> str:
    base_pattern = [0, 1, 0, -1]
    curr = n

    if debug:
        print(f"Input signal: {curr}\n")

    for phase in range(n_phases):
        next = ""

        for pos in range(1, len(curr) + 1):
            msg = ""
            num = 0

            for idx in range(len(curr)):
                p = ((idx + 1) // pos) % len(base_pattern)
                coeff = base_pattern[p]

                msg += f"{curr[idx]}*{coeff}".ljust(5) + (
                    "+ " if idx < len(curr) - 1 else "= "
                )
                num += coeff * int(curr[idx])

            digit = abs(num) % 10
            next += str(digit)

            if debug:
                print(f"{msg}{digit}")

        curr = next

        if debug:
            print(f"After {phase} phases: {curr}\n")

    return curr


def part1(input: str) -> str:
    result = fft(input, 100)
    return result[:8]


def part2(input: str) -> str:
    # Start from the offset of the first 8 digits of the expanded input
    offset = int(input[:7])
    input *= 10_000
    input = input[offset:]

    curr = input

    for _ in range(100):
        next = ""
        s = sum(int(digit) for digit in curr)

        for digit in curr:
            next += f"{((s % 10) + 10) % 10}"
            s -= int(digit)

        curr = next

    return curr[:8]


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    part2("03036732577212944063491565474664")
