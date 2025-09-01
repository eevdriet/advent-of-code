from typing import List


def sonar_sweep(depths: List[int], *, offset: int):
    return sum(second > first for first, second in zip(depths, depths[offset:]))


def main():
    depths = [int(depth) for depth in open("data/01.input").readlines()]

    print(f"Part 1: {sonar_sweep(depths, offset=1)}")
    print(f"Part 2: {sonar_sweep(depths, offset=3)}")


if __name__ == "__main__":
    main()

