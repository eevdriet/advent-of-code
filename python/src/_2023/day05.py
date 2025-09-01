from typing import List, Tuple

Seed = int
Block = List[Tuple[int, int, int]]


def parse(txt: str) -> Tuple[List[Seed], List[Block]]:
    seeds, *block_strs = txt.split("\n\n")
    seeds = list(map(int, seeds.split(":")[1].split()))

    blocks = []

    for block_str in block_strs:
        block = []

        for line in block_str.splitlines()[1:]:
            l, m, r = map(int, line.split())
            block.append((l, m, r))

        blocks.append(block)

    return seeds, blocks


def part1(inputs: List[Seed], blocks: List[Block]) -> int:
    seeds = inputs.copy()

    for block in blocks:
        new = []

        for seed in seeds:
            for l, m, r in block:
                if seed in range(m, m + r):
                    new.append(seed - m + l)
                    break
            else:
                new.append(seed)

        seeds = new

    return min(seeds)


def part2(inputs: List[Seed], blocks: List[Block]) -> int:
    seeds = []

    for idx in range(0, len(inputs), 2):
        seeds.append((inputs[idx], inputs[idx] + inputs[idx + 1]))

    for block in blocks:
        new = []

        while len(seeds) > 0:
            start, end = seeds.pop()

            for l, m, r in block:
                os = max(start, m)
                oe = min(end, m + r)

                if os < oe:
                    new.append((os - m + l, oe - m + l))

                    if os > start:
                        seeds.append((start, os))
                    if oe < end:
                        seeds.append((oe, end))

                    break
            else:
                new.append((start, end))

        seeds = new

    return min(seeds)[0]


def main():
    seeds, blocks = parse(open("data/5.input").read())

    print(f"Part 1: {part1(seeds, blocks)}")
    print(f"Part 2: {part2(seeds, blocks)}")


if __name__ == "__main__":
    main()

