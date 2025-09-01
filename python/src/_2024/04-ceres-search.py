from aoc.io import FileType, open_file


def search1(grid: list[str], row: int, col: int) -> int:
    count = 0
    TARGET = "XMAS"

    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            if r == c == 0:
                continue
            if not (0 <= row + (len(TARGET) - 1) * r < len(grid)):
                continue
            if not (0 <= col + (len(TARGET) - 1) * c < len(grid[row])):
                continue

            count += all(
                grid[row + n * r][col + n * c] == TARGET[n] for n in range(len(TARGET))
            )

    return count


def search2(grid: list[str], row: int, col: int) -> bool:
    TARGETS = ["MAS", "SAM"]

    if row + len(TARGETS[0]) - 1 >= len(grid):
        return False
    if col + len(TARGETS[0]) - 1 >= len(grid[row]):
        return False

    if any(
        all(grid[row + n][col + n] == target[n] for n in range(len(target)))
        for target in TARGETS
    ) and any(
        all(
            grid[row + len(target) - 1 - n][col + n] == target[n]
            for n in range(len(target))
        )
        for target in TARGETS
    ):
        return True

    return False


def part1(grid: list[str]) -> int:
    return sum(
        search1(grid, row, col)
        for row in range(len(grid))
        for col in range(len(grid[row]))
    )


def part2(grid: list[str]) -> int:
    return sum(
        search2(grid, row, col)
        for row in range(len(grid))
        for col in range(len(grid[row]))
    )


def main():
    with open_file(2024, 4, FileType.INPUT) as file:
        grid = file.readlines()

    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")


if __name__ == "__main__":
    main()
