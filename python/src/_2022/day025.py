from typing import List

FileSystem = dict[str, int]


def parse(input: str) -> list[str]:
    return input.splitlines()


def search_files(lines: list[str]) -> dict[str, int]:
    return {}


def part1(lines: List[str]):
    pass


def part2(lines: List[str]):
    pass


def main():
    lines = open("data/5.input").read().strip().splitlines()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()

