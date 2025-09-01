import sys
from hashlib import md5

from aoc.util import timed


def parse(input: str) -> str:
    return input


def part1(door_id: str) -> str:
    idx = 0
    hash = ""
    password = []

    while len(password) < 8:
        data = f"{door_id}{idx}"
        hash = md5(data.encode()).hexdigest()
        idx += 1

        if hash[:5] == "00000":
            password.append(hash[5])

    return "".join(password)


def part2(door_id: str) -> str:
    idx = 0
    hash = ""

    # Keep track of how many letters of the password are filled
    password = [""] * 8
    digest = md5()
    digest.update(door_id.encode())

    while any(digit == "" for digit in password):
        # Find next hash
        curr = digest.copy()
        curr.update(str(idx).encode())

        hash = curr.hexdigest()
        idx += 1

        # Only fill in blank spots once the hash reached 5 leading zeroes
        fill_idx = int(hash[5], 16)

        if (
            hash.startswith("00000")
            and fill_idx < len(password)
            and password[fill_idx] == ""
        ):
            password[fill_idx] = hash[6]

    return "".join(password)


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
