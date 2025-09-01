from typing import *
from collections import defaultdict
from itertools import accumulate
import sys


def no_space_left_on_device(dirs: Dict[str, int]) -> int:
    return sum(size for size in dirs.values() if size <= 100_000)

def no_space_left_on_device2(dirs: Dict[str, int]) -> int:
    return min(size for size in dirs.values() if size >= dirs['/'] - 40_000_000)

def main():
    lines = [line.strip() for line in sys.stdin]

    dirs = defaultdict(int)
    path = []

    for line in lines:
        match line.split():
            case '$', 'cd', '/':
                path = ['/']
            case '$', 'cd', '..':
                path.pop()
            case '$', 'cd', dir:
                path.append(dir + '/')
            case '$', 'ls':
                pass
            case 'dir', _:
                pass
            case size, _:
                for p in accumulate(path):
                    dirs[p] += int(size)

    print(no_space_left_on_device(dirs))
    print(no_space_left_on_device2(dirs))

if __name__ == '__main__':
    main()