import re
import sys
from collections import deque
from functools import reduce
from hashlib import md5

from aoc.util import timed


def parse(input: str) -> str:
    return input


def get_hash(salt: str, n_repeats: int) -> str:
    for _ in range(n_repeats):
        salt = md5(salt.encode()).hexdigest()

    return salt


def find_keys(salt: str, n_repeats: int = 1) -> int:
    idx = 0
    n_found = 0

    # Use a rolling array of hashes
    hashes = deque([get_hash(f"{salt}{idx}", n_repeats) for idx in range(1001)])

    while True:
        # Consider a hash and find whether it has a triplet
        hash = hashes.popleft()
        triple = re.search(r"(.)\1\1", hash)

        if triple:
            # If so, for it to be a key there must be another hash with that quintuplet
            ch = triple.group(1)

            if any(ch * 5 in hash for hash in hashes):
                # If so, we've found a key and can stop if 64 are found
                n_found += 1
                if n_found == 64:
                    break

        # Add the next hash to keep the rolling array working
        hash = get_hash(f"{salt}{idx + 1000}", n_repeats)
        hashes.append(hash)

        idx += 1

    return idx - 1


def part1(salt: str) -> int:
    return find_keys(salt, n_repeats=1)


def part2(salt: str) -> int:
    return find_keys(salt, n_repeats=2017)


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
