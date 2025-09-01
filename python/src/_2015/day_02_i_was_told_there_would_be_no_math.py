import sys

from aoc.util import timed


class Box:
    def __init__(self, length: int, width: int, height: int):
        self.length = length
        self.width = width
        self.height = height

    @property
    def surface_area(self) -> int:
        l, w, h = self.length, self.width, self.height

        return (2 * l * w) + (2 * w * h) + (2 * h * l)

    @property
    def paper_needed(self) -> int:
        l, w, h = self.length, self.width, self.height

        return self.surface_area + min(l * w, w * h, h * l)

    @property
    def volume(self) -> int:
        return self.length * self.width * self.height

    @property
    def smallest_perimeter(self) -> int:
        dimensions = [self.length, self.width, self.height]
        dimensions.sort()

        return 2 * sum(dimensions[:2])

    @property
    def ribbon_needed(self) -> int:
        return self.smallest_perimeter + self.volume


def parse(input: str) -> list[Box]:
    return [Box(*map(int, line.split("x"))) for line in input.splitlines()]


def part1(boxes: list[Box]) -> int:
    return sum(box.paper_needed for box in boxes)


def part2(boxes: list[Box]):
    return sum(box.ribbon_needed for box in boxes)


def main():
    input = sys.stdin.read()
    boxes = parse(input)

    result1, elapsed = timed(part1, boxes)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, boxes)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
