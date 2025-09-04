import sys

from aoc.util import timed

Point = tuple[int, int, int, int]


def parse(input: str) -> list[Point]:
    return [tuple(map(int, line.split(","))) for line in input.splitlines()]


class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node: int) -> int:
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def unite(self, x: int, y: int):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[y_root] < self.rank[x_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1


def part1(points: list[Point]) -> int:
    n = len(points)
    uf = UnionFind(n)

    def manhattan(a: tuple[int, ...], b: tuple[int, ...]) -> int:
        assert len(a) == len(b)
        return sum(abs(x - y) for x, y in zip(a, b))

    for i in range(n):
        for j in range(i + 1, n):
            point1 = points[i]
            point2 = points[j]

            if manhattan(point1, point2) <= 3:
                uf.unite(i, j)

    roots = {uf.find(i) for i in range(n)}
    return len(roots)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
