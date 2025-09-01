import sys

from aoc.util import timed

Component = tuple[int, int]


def parse(input: str) -> set[Component]:
    components = set()

    for line in input.splitlines():
        src, dst = map(int, line.split("/"))
        components.add((src, dst))
        components.add((dst, src))

    return components


def find_bridge(components: set[Component], *, part2: bool = False) -> int:
    max_strength = 0
    longest = 0
    max_longest_strength = 0

    def find_connecting(last: int):
        return [(src, dst) for src, dst in components if src == last]

    def backtrack(bridge: list[Component]):
        nonlocal max_strength, max_longest_strength, longest
        _, target = bridge[-1]

        # Try to find connecting component
        next_components = find_connecting(target)

        # Cannot build further: try to find stronger bridge
        if len(next_components) == 0:
            strength = sum(src + dst for src, dst in bridge)
            max_strength = max(strength, max_strength)

            if len(bridge) > longest:
                longest = len(bridge)
                max_longest_strength = strength
            elif len(bridge) == longest:
                max_longest_strength = max(max_longest_strength, strength)

        for src, dst in next_components:
            next = (src, dst)
            next_rev = (dst, src)

            components.remove(next)
            components.discard(next_rev)

            backtrack(bridge + [next])

            components.add(next_rev)
            components.add(next)

    backtrack([(0, 0)])
    return max_longest_strength if part2 else max_strength


def part1(components: set[Component]) -> int:
    return find_bridge(components, part2=False)


def part2(components: set[Component]) -> int:
    return find_bridge(components, part2=True)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
