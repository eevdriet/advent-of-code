import sys

from aoc.io import read_file
from aoc.util import timed

Pattern = str
Output = str
Entry = tuple[list[Pattern], list[Output]]


def parse(input: str) -> list[Entry]:
    entries = []

    for line in input.splitlines():
        patterns_text, output_text = line.split(" | ")

        patterns = patterns_text.split()
        outputs = output_text.split()

        entry = patterns, outputs
        entries.append(entry)

    return entries


def part1(entries: list[Entry]) -> int:
    uniq_digit_lens = {"1": 2, "7": 3, "4": 4, "8": 7}

    total_1748 = 0

    for _, outputs in entries:
        total_1748 += sum(
            bool(len(output) in uniq_digit_lens.values()) for output in outputs
        )

    return total_1748


def part2(entries: list[Entry]) -> int:
    total = 0

    for patterns, outputs in entries:
        pattern_sets = [set(p) for p in patterns]
        digit_patterns = {}

        # Step 1: deduce digits with unique-length patterns
        for pattern in pattern_sets:
            match len(pattern):
                case 2:
                    digit_patterns[1] = pattern
                case 3:
                    digit_patterns[7] = pattern
                case 4:
                    digit_patterns[4] = pattern
                case 7:
                    digit_patterns[8] = pattern

                case _:
                    pass

        # Step 2: deduce remaining digits
        for pattern in pattern_sets:
            if pattern in digit_patterns.values():
                continue

            match len(pattern):
                # 3 contains all segments of 1
                case 5 if digit_patterns[1] <= pattern:
                    dst = 3
                # 5 contains 3 of the segments of 4
                case 5 if len(pattern & digit_patterns[4]) == 3:
                    dst = 5
                # 5 is the remaining option with 5 sides
                case 5:
                    dst = 2

                # 9 contains all segments of 4
                case 6 if digit_patterns[4] <= pattern:
                    dst = 9
                # 0 contains all segments of 1
                case 6 if digit_patterns[1] <= pattern:
                    dst = 0
                # 6 is the remaining option with 6 sides
                case 6:
                    dst = 6

                case _:
                    raise ValueError(f"Cannot deduce digit from pattern '{pattern}'")

            digit_patterns[dst] = pattern

        # Now map the patterns to digits to read the number from all outputs
        pattern_digits = {frozenset(p): str(d) for d, p in digit_patterns.items()}

        num = "".join(pattern_digits[frozenset(o)] for o in outputs)
        total += int(num)

    return total


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2021, 8, "example2")
    part2(parse(input))
