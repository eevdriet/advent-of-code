import sys
from typing import Optional

from attrs import define, field

from aoc.util import timed


@define
class TreeNode:
    id: str
    parent: Optional["TreeNode"] = field(default=None)
    children: list["TreeNode"] = field(factory=lambda: [])

    def __hash__(self):
        return hash(self.id)


def parse(input: str) -> dict[str, TreeNode]:
    nodes: dict[str, TreeNode] = {}

    for line in input.splitlines():
        parent, child = line.split(")")

        if parent not in nodes:
            nodes[parent] = TreeNode(parent)
        if child not in nodes:
            nodes[child] = TreeNode(child)

        nodes[parent].children.append(nodes[child])
        nodes[child].parent = nodes[parent]

    return nodes


def part1(nodes: dict[str, TreeNode]) -> int:
    root = next((node for node in nodes.values() if node.parent is None))

    n_orbits = 0
    stack = [(root, 0)]

    while stack:
        node, depth = stack.pop()
        n_orbits += depth

        for child in node.children:
            stack.append((child, depth + 1))

    return n_orbits


def part2(nodes: dict[str, TreeNode]) -> int:
    you = nodes["YOU"]
    santa = nodes["SAN"]

    node = you.parent
    n_steps = 0

    ancestors = {}

    while node is not None:
        n_steps += 1
        node = node.parent

        ancestors[node] = n_steps

    node = santa.parent
    n_steps = 0

    while node is not None and node not in ancestors:
        n_steps += 1
        node = node.parent

    return n_steps + ancestors[node]


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
