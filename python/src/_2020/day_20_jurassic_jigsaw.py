import operator
import sys
from collections import defaultdict
from functools import reduce
from math import prod, sqrt

import parse as ps
from attrs import define, field

from aoc.util import timed


@define
class Tile:
    id: int
    image: list[str]
    edges: list[int] = field(factory=lambda: [])

    def flipped(self) -> "Tile":
        flipped_image = [row[::-1] for row in self.image]
        return Tile(self.id, flipped_image)

    def rotated(self) -> "Tile":
        size = len(self.image)
        rotated_image = [
            "".join(self.image[size - row - 1][col] for row in range(size))
            for col in range(size)
        ]
        return Tile(self.id, rotated_image)

    def borderless(self) -> "Tile":
        borderless_image = [row[1:-1] for row in self.image[1:-1]]
        return Tile(self.id, borderless_image)

    def orientations(self) -> list["Tile"]:
        # Flip and rotate to get all 8 possible orientations
        result = []
        tile = self

        for _ in range(4):  # 4 rotations
            result.append(tile)
            result.append(tile.flipped())
            tile = tile.rotated()

        # Deduplicate the result
        unique = []
        seen = set()

        for tile in result:
            key = tuple(tile.image)
            if key not in seen:
                seen.add(key)
                unique.append(tile)

        return unique

    @property
    def size(self):
        return len(self.image)

    @property
    def top(self) -> str:
        return self.image[0]

    @property
    def bottom(self) -> str:
        return self.image[-1]

    @property
    def left(self) -> str:
        return "".join(row[0] for row in self.image)

    @property
    def right(self) -> str:
        return "".join(row[-1] for row in self.image)

    def __attrs_post_init__(self):
        """Return the 4 edges (both normal and reversed)."""
        str_edges = [self.top, self.bottom, self.left, self.right]

        for str_edge in str_edges:
            normal = self._edge_to_int(str_edge)
            reverse = self._edge_to_int(str_edge[::-1])

            self.edges.append(normal)
            self.edges.append(reverse)

        return self.edges

    def _edge_to_int(self, edge: str) -> int:
        return sum(1 << bit for bit, cell in enumerate(edge) if cell == "#")


@define
class TileMerger:
    tiles: list[Tile]
    edge_counts: dict[int, int] = field(factory=lambda: defaultdict(int))

    def find_corners(self) -> list[Tile]:
        # Corner tiles: exactly 2 unique edges (which appear only once globally)
        corners = []

        for tile in self.tiles:
            unique_edges = sum(1 for edge in tile.edges if self.edge_counts[edge] == 1)

            # Each edge counted twice (normal + reversed), so we need 4 here
            if unique_edges == 4:
                corners.append(tile)

        assert len(corners) == 4
        return corners

    def merge(self, tile_id: int) -> Tile:
        grid_size = int(sqrt(len(self.tiles)))
        tile_grid: list[list[Tile]] = [[None] * grid_size for _ in range(grid_size)]

        corner_ids = {corner.id for corner in self.find_corners()}
        used_tiles = set()

        def fits(tile: Tile, row: int, col: int) -> bool:
            # Should be corner
            if (row, col) in [
                (0, 0),
                (0, grid_size - 1),
                (grid_size - 1, 0),
                (grid_size - 1, grid_size - 1),
            ] and tile.id not in corner_ids:
                return False

            # Should match above
            if row > 0 and tile_grid[row - 1][col].bottom != tile.top:
                return False

            # Should match to the left
            if col > 0 and tile_grid[row][col - 1].right != tile.left:
                return False

            return True

        def backtrack(pos: int) -> bool:
            if pos == grid_size * grid_size:
                return True

            row, col = divmod(pos, grid_size)

            for tile in self.tiles:
                if tile.id in used_tiles:
                    continue

                for orientation in tile.orientations():
                    if not fits(orientation, row, col):
                        continue

                    tile_grid[row][col] = orientation
                    used_tiles.add(orientation.id)

                    if backtrack(pos + 1):
                        return True

                    tile_grid[row][col] = None
                    used_tiles.remove(orientation.id)

            return False

        if not backtrack(0):
            raise RuntimeError("Could not merge tiles into a single tile")

        assert all(tile is not None for row_tiles in tile_grid for tile in row_tiles)

        # Merge the tiles together from their merged image
        tile_grid = [
            [tile.borderless() for tile in row_tiles] for row_tiles in tile_grid
        ]

        image_size = tile_grid[0][0].size

        merged_image = [
            reduce(operator.add, (tile.image[idx] for tile in row_tiles), "")
            for row_tiles in tile_grid
            for idx in range(image_size)
        ]

        return Tile(tile_id, merged_image)

    def __attrs_post_init__(self):
        for tile in self.tiles:
            for edge in tile.edges:
                self.edge_counts[edge] += 1


def parse(input: str) -> list[Tile]:
    blocks = input.strip().split("\n\n")
    tiles = []

    for block in blocks:
        id_line, *grid = block.splitlines()
        tile_id = ps.parse("Tile {:d}:", id_line)[0]

        tile = Tile(tile_id, grid)
        tiles.append(tile)

    return tiles


def part1(tiles: list[Tile]) -> int:
    merger = TileMerger(tiles)
    corners = merger.find_corners()

    return prod(corner.id for corner in corners)


SEA_MONSTER = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""
SEA_MONSTER_IMAGE = [row for row in SEA_MONSTER.splitlines() if row]
N_SEA_MONSTER_HASHES = SEA_MONSTER.count("#")


def part2(tiles: list[Tile]) -> int:
    merger = TileMerger(tiles)
    merged_tile = merger.merge(0)

    def overlay(tile: Tile, row: int, col: int) -> bool:
        for r in range(len(SEA_MONSTER_IMAGE)):
            for c in range(len(SEA_MONSTER_IMAGE[0])):
                if (
                    SEA_MONSTER_IMAGE[r][c] == "#"
                    and tile.image[row + r][col + c] != "#"
                ):
                    return False

        return True

    n_hashes = sum(row.count("#") for row in merged_tile.image)

    for tile in merged_tile.orientations():
        n_sea_monsters = 0
        row = 0

        for row in range(len(tile.image) - len(SEA_MONSTER_IMAGE)):
            for col in range(tile.size - len(SEA_MONSTER_IMAGE[0])):
                if overlay(tile, row, col):
                    n_sea_monsters += 1

        if n_sea_monsters > 0:
            return n_hashes - n_sea_monsters * N_SEA_MONSTER_HASHES

    raise RuntimeError("Couldn't find any sea monsters!")


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
