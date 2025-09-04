import sys

from aoc.util import timed


def parse(input: str) -> str:
    return input.strip()


def run(*, part2: bool = False) -> int:
    seen = set()
    last = None

    r2 = 0
    while True:
        r5 = r2 | 65536
        r2 = 16123384

        while True:
            r2 = (((r2 + (r5 & 255)) & 0xFFFFFF) * 65899) & 0xFFFFFF

            if r5 < 256:
                # <-- line 28 comparison would happen here (eqrr 2 0 3)
                if not seen and not part2:
                    return r2

                if r2 in seen and part2 and last:
                    return last

                seen.add(r2)
                last = r2
                break

            else:
                r5 //= 256


def part1(input: str) -> int:
    return run(part2=False)


def part2(input: str) -> int:
    return run(part2=True)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
