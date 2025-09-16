import sys
from collections.abc import Generator
from itertools import combinations, permutations, product

from attrs import define, field

from aoc.util import timed

Coord = tuple[int, int, int]
Beacon = tuple[int, ...]


def _generate_rotations():
    rotations = []

    for perm in permutations((0, 1, 2)):
        for signs in product([1, -1], repeat=3):

            def rotation(
                beacon: Beacon,
                perm: tuple[int, ...] = perm,
                signs: tuple[int, ...] = signs,
            ):
                return tuple(beacon[i] * s for i, s in zip(perm, signs))

            # check determinant to filter reflections
            x, y, z = rotation((1, 0, 0)), rotation((0, 1, 0)), rotation((0, 0, 1))
            det = (
                x[0] * (y[1] * z[2] - y[2] * z[1])
                - x[1] * (y[0] * z[2] - y[2] * z[0])
                + x[2] * (y[0] * z[1] - y[1] * z[0])
            )
            if det == 1:
                rotations.append(rotation)

    return rotations


_ROTATIONS = _generate_rotations()


@define(slots=True, eq=False, hash=False)
class Scanner:
    id: int
    beacons: list[Coord]
    pos: Coord | None = field(default=None)

    def orientations(self) -> Generator[list[Beacon]]:
        for rotate in _ROTATIONS:
            yield [rotate(beacon) for beacon in self.beacons]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Scanner):
            return NotImplemented

        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)


def parse(input: str) -> list[Scanner]:
    scanners = []

    for id, scanner_block in enumerate(input.strip().split("\n\n")):
        _, *beacon_lines = scanner_block.splitlines()

        beacons = []
        for line in beacon_lines:
            x, y, z = map(int, line.split(","))
            beacons.append((x, y, z))

        scanner = Scanner(id, beacons)
        scanners.append(scanner)

    return scanners


def locate_beacons(scanners: list[Scanner]) -> set[Coord]:
    # Fix the first scanner at the origin
    first_scanner, *other_scanners = scanners
    first_scanner.pos = (0, 0, 0)

    # Then keep track of which scanners are placed and unplaced, as well as located beacons
    placed = {first_scanner}
    unplaced = {scanner for scanner in other_scanners}
    beacons = set(scanners[0].beacons)

    def place_next_scanner() -> bool:
        for scanner in list(unplaced):
            for oriented_beacons in scanner.orientations():
                offsets = {}

                for a, b in product(beacons, oriented_beacons):
                    # Determine the relative offset
                    offset = (a[0] - b[0], a[1] - b[1], a[2] - b[2])
                    offsets[offset] = offsets.get(offset, 0) + 1

                    if offsets[offset] < 12:
                        continue

                    # Found alignment!
                    scanner.pos = offset
                    translated = [
                        (bx + offset[0], by + offset[1], bz + offset[2])
                        for (bx, by, bz) in oriented_beacons
                    ]
                    beacons.update(translated)
                    placed.add(scanner)
                    unplaced.remove(scanner)

                    return True

        return False

    # Keep placing scanners until all are placed
    while unplaced:
        if not place_next_scanner():
            raise RuntimeError("Could not place all scanners")

    return beacons


def part1(scanners: list[Scanner]) -> int:
    beacons = locate_beacons(scanners)
    return len(beacons)


def part2(scanners: list[Scanner]) -> int:
    # Place all scanners and verify its success
    _ = locate_beacons(scanners)
    assert all(scanner.pos is not None for scanner in scanners)

    # Then simply calculate the maximal distance between any two
    max_dist = 0

    for first, second in combinations(scanners, 2):
        x1, y1, z1 = first.pos
        x2, y2, z2 = second.pos

        dist = abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)
        if dist > max_dist:
            max_dist = dist

    return max_dist


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
