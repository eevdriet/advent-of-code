import sys

from attrs import define, field

from aoc.io import open_file
from aoc.util import timed


@define
class Node:
    id: str
    metadata: list[int] = field(factory=lambda: [])
    children: list["Node"] = field(factory=lambda: [])


def parse(input: str) -> Node:
    nums = [int(num) for num in input.split()]
    count = 0

    def dfs(id: int, pos: int) -> tuple[Node, int]:
        nonlocal count

        n_children = nums[pos]
        n_metadata = nums[pos + 1]
        pos += 2

        node = Node(chr(ord("A") + count))

        for _ in range(n_children):
            count += 1
            child, pos = dfs(id, pos)
            node.children.append(child)

        for idx in range(n_metadata):
            node.metadata.append(nums[pos + idx])

        return node, pos + n_metadata

    root, _ = dfs(0, 0)
    return root


def part1(root: Node) -> int:
    def dfs(node: Node) -> int:
        return sum(node.metadata) + sum([dfs(child) for child in node.children])

    return dfs(root)


def part2(root: Node) -> int:
    memo = {}

    def dfs(node: Node) -> int:
        if node.id in memo:
            return memo[node.id]

        if not node.children:
            memo[node.id] = sum(node.metadata)
            return memo[node.id]

        result = 0

        for entry in node.metadata:
            idx = entry - 1

            if idx in range(len(node.children)):
                result += dfs(node.children[idx])

        memo[node.id] = result
        return memo[node.id]

    return dfs(root)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    with open_file(2018, 8) as file:
        part2(parse(file.read()))
