from math import prod
from typing import List


def part1(lines: List[str]) -> int:
    total = 0
    max_seen = {"red": 12, "green": 13, "blue": 14}

    for id, line in enumerate(lines, 1):
        groups = line.strip().split(": ")[1].split("; ")

        for group in groups:
            seen = {"red": 0, "green": 0, "blue": 0}

            for elem in group.split(", "):
                count, color = elem.split()
                seen[color] = int(count)

            if any(seen[color] > max_seen[color] for color in seen):
                break
        else:
            total += id

    return total


def part2(lines: List[str]) -> int:
    total = 0

    for line in lines:
        max_seen = {"red": 0, "green": 0, "blue": 0}
        groups = line.strip().split(": ")[1].split("; ")

        for group in groups:
            seen = {"red": 0, "green": 0, "blue": 0}

            for elem in group.split(", "):
                count, color = elem.split()
                seen[color] = int(count)

            for color in max_seen:
                max_seen[color] = max(seen[color], max_seen[color])

        total += prod(max_seen.values())

    return total


def main():
    lines = open("data/2.input").read().strip().splitlines()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()

