import sys

from aoc.util import timed


def parse(input: str) -> str:
    return input


def apply_dragon(a: str) -> str:
    b = "".join(str(1 - int(digit)) for digit in reversed(a))
    return f"{a}0{b}"


def apply_checksum(num: str) -> str:
    return "".join(
        "1" if num[idx] == num[idx + 1] else "0" for idx in range(0, len(num), 2)
    )


def find_checksum(num: str, disk_len: int) -> str:
    # Apply the dragon curve until we can fill the disk
    while len(num) < disk_len:
        num = apply_dragon(num)

    num = num[:disk_len]

    # Then apply the checksum algorithm until the result is of odd length
    while True:
        num = apply_checksum(num)
        if len(num) & 1:
            break

    return num


def part1(num: str) -> str:
    return find_checksum(num, 272)


def part2(num: str) -> str:
    return find_checksum(num, 35651584)


if __name__ == "__main__":
    input = sys.stdin.read()
    num = parse(input)

    result1, elapsed = timed(part1, num)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, num)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
