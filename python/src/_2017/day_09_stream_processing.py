import sys

from aoc.util import timed


def parse(input: str) -> str:
    return input.strip()


def find_in_groups(groups: str, part2: bool) -> int:
    score = 0
    n_garbage = 0

    pos = 0
    depth = 0

    while pos < len(groups):
        match groups[pos]:
            # Start a new valid group
            case "{":
                depth += 1

            # Close an existing valid group
            case "}":
                score += depth
                depth -= 1

            # Enter garbage group
            case "<":
                pos += 1

                while pos < len(groups):
                    # Skip over ignored characters with !
                    if groups[pos] == "!":
                        pos += 2
                        continue

                    # Close garbage group
                    if groups[pos] == ">":
                        break

                    n_garbage += 1
                    pos += 1

        pos += 1

    return n_garbage if part2 else score


def part1(groups: str) -> int:
    return find_in_groups(groups, part2=False)


def part2(groups: str) -> int:
    return find_in_groups(groups, part2=True)


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
