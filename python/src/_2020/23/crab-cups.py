from typing import *
import sys


def crab_cups(cups: List[int], *, n_rounds: int):
    current = cups[0]
    mn, mx = min(cups), max(cups)
    carousel = dict(zip(cups, cups[1:] + cups[:1]))

    for _ in range(n_rounds):
        xyz = [carousel[current]]
        xyz.append(carousel[xyz[0]])
        xyz.append(carousel[xyz[-1]])
        dest = current - 1
        while dest < mn or dest in xyz:
            dest -= 1
            if dest < mn:
                dest = mx
        carousel[current] = carousel[xyz[-1]]
        carousel[xyz[-1]] = carousel[dest]
        carousel[dest] = xyz[0]
        current = carousel[current]

    return carousel

def main():
    old_cups = [int(cup) for cup in sys.stdin.read().strip()]
    cups = crab_cups(old_cups, n_rounds=100)
    labels = [cups[1]]
    while labels[-1] != 1:
        labels.append(cups[labels[-1]])

    print('Part One:', "".join([str(c) for c in labels[:-1]]))
    
    cups = crab_cups(old_cups + list(range(9+1, 1_000_001)), n_rounds=10_000_000)
    c1 = cups[1]
    c2 = cups[c1]
    print('Part Two:', c1 * c2)

if __name__ == '__main__':
    main()