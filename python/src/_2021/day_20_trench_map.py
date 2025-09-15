import sys

from attrs import define

from aoc.util import timed


@define
class Image:
    enhancement: str
    pixels: set[complex]
    default_pixel: str = "."

    def enhance(self, is_on: bool):
        x_min = int(min(p.real for p in self.pixels))
        x_max = int(max(p.real for p in self.pixels))
        y_min = int(min(p.imag for p in self.pixels))
        y_max = int(max(p.imag for p in self.pixels))

        directions = [
            -1 - 1j,
            0 - 1j,
            1 - 1j,
            -1 + 0j,
            0 + 0j,
            1 + 0j,
            -1 + 1j,
            0 + 1j,
            1 + 1j,
        ]

        new_pixels = set()

        for y in range(y_min - 5, y_max + 10):
            for x in range(x_min - 5, x_max + 10):
                pos = complex(x, y)
                bits = []

                for d in directions:
                    neighbor = pos + d
                    bits.append("1" if (neighbor in self.pixels) == is_on else "0")

                idx = int("".join(bits), 2)
                if (self.enhancement[idx] == "#") != is_on:
                    new_pixels.add(pos)

        if self.default_pixel == ".":
            self.default_pixel = self.enhancement[0]
        else:
            self.default_pixel = self.enhancement[-1]

        self.pixels = new_pixels


def parse(input: str) -> Image:
    enhancement, pixels_text = input.split("\n\n")
    pixels = {
        complex(x, y)
        for y, line in enumerate(pixels_text.splitlines())
        for x, cell in enumerate(line)
        if cell == "#"
    }

    return Image(enhancement.strip(), pixels)


def enhance(image: Image, n_steps: int):
    flip = image.enhancement[0] == "#" and image.enhancement[-1] == "."
    is_on = True

    for step in range(n_steps):
        image.enhance(is_on)

        if flip:
            is_on = not is_on

    return len(image.pixels)


def part1(image: Image) -> int:
    return enhance(image, n_steps=2)


def part2(image: Image) -> int:
    return enhance(image, n_steps=50)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
