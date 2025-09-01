import sys

from aoc.util import timed


def parse(input: str) -> str:
    return input


class Password:
    def __init__(self, repr: str):
        self.repr = repr

    def is_valid(self):
        # Three increasing
        has_3_increase = False

        for idx in range(len(self.repr) - 2):
            if (
                ord(self.repr[idx])
                == ord(self.repr[idx + 1]) - 1
                == ord(self.repr[idx + 2]) - 2
            ):
                has_3_increase = True
                break

        if not has_3_increase:
            return False

        # Forbidden letters
        forbidden = "iol"
        if any(letter in forbidden for letter in self.repr):
            return False

        # Non-overlapping pairs
        has_non_overlap_pairs = False

        pairs = set()
        for pos in range(len(self.repr) - 1):
            pair = self.repr[pos : pos + 2]
            if pair[0] != pair[1]:
                continue

            if pairs and pair not in pairs:
                has_non_overlap_pairs = True
                break
            else:
                pairs.add(pair)

        if not has_non_overlap_pairs:
            return False

        return True

    def __str__(self):
        return self.repr

    def _generate_next(self):
        repr = list(self.repr)

        for idx in reversed(range(len(repr))):
            if repr[idx] < "z":
                repr[idx] = chr(ord(repr[idx]) + 1)
                self.repr = "".join(repr)
                return

            repr[idx] = "a"

        self.repr = "a" + "".join(repr)

    def next(self):
        while not self.is_valid():
            self._generate_next()

        return self


def part1(repr: str) -> str:
    password = Password(repr)

    return password.next().repr


def part2(repr: str) -> str:
    password = Password(repr)
    first = password.next()

    first._generate_next()
    second = password.next()

    return second.repr


def main():
    input = sys.stdin.read()
    repr = parse(input)

    result1, elapsed = timed(part1, repr)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, repr)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
