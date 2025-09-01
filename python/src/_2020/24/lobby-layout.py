from typing import *
import sys
import re

direction_map = {
    'e': 2 + 0j,
    'w': -2 + 0j,
    'ne': 1 - 2j,
    'nw': -1 - 2j,
    'se': 1 + 2j,
    'sw': -1 + 2j
}

def adjacent(position: complex):
    for direction in direction_map.values():
        yield position + direction

def move(directions: List[str]):
    position = 0 + 0j

    for direction in directions:
        position += direction_map[direction]
        
    return position

def lobby_layout(flips: List[List[str]]):
    tiles = set()
    
    for directions in flips:
        position = move(directions)
        tiles ^= {position}
        
    return tiles

def lobby_layout2(flips: List[List[str]], *, n_days: int):
    tiles = lobby_layout(flips)
    
    for _ in range(n_days):
        tile_counts = {}
        for tile in tiles:
            for neighbor in adjacent(tile):
                tile_counts[neighbor] = 1 + tile_counts.get(neighbor, 0)

        stay_black = {tile for tile in tiles if tile_counts.get(tile, 0) in (1, 2)}
        turn_black = {tile for tile, count in tile_counts.items() if tile not in tiles and count == 2}
        tiles = stay_black | turn_black
        
    return tiles

def main():
    lines = sys.stdin.readlines()
    flips = [[flip for flip in re.findall(r'(se|sw|nw|ne|e|w)', line.strip())] for line in lines]
    
    print(len(lobby_layout(flips)))
    print(len(lobby_layout2(flips, n_days=100)))

if __name__ == '__main__':
    main()