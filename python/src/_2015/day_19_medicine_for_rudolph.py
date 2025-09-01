import sys
from collections import defaultdict

from aoc.util import timed

Molecule = str
Replacements = dict[Molecule, set[Molecule]]


def parse(input: str) -> tuple[Molecule, Replacements]:
    replacements_str, molecule = input.split("\n\n")
    replacements = defaultdict(set)

    for line in replacements_str.splitlines():
        left, right = line.split(" => ")
        replacements[left].add(right)

    return molecule, replacements


def part1(molecule: str, substitutes: Replacements) -> int:
    seen = set()

    for left, rights in substitutes.items():
        for idx in range(len(molecule) - len(left)):
            if molecule[idx : idx + len(left)] == left:
                for right in rights:
                    new_molecule = molecule[:idx] + right + molecule[idx + len(left) :]
                    seen.add(new_molecule)

    return len(seen)


def part2(molecule: str, _: Replacements) -> int:
    n_molecules = sum(1 for ch in molecule if ch.isupper())

    return (
        n_molecules
        - molecule.count("Rn")
        - molecule.count("Ar")
        - 2 * molecule.count("Y")
        - 1
    )


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, *parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
