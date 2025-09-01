from typing import *
from collections import Counter
import sys
import re

Reboot = Tuple[bool, Tuple[int, int, int, int, int, int]]

def reactor_reboot(reboots: List[Reboot]) -> int:
    cubes = Counter()

    for on, (nx0, nx1, ny0, ny1, nz0, nz1) in reboots:
        nsgn = 1 if on else -1
        new_cubes = Counter()

        for (ex0, ex1, ey0, ey1, ez0, ez1), esgn in cubes.items():
            ix0 = max(nx0, ex0); ix1 = min(nx1, ex1)
            iy0 = max(ny0, ey0); iy1 = min(ny1, ey1)
            iz0 = max(nz0, ez0); iz1 = min(nz1, ez1)

            if ix0 <= ix1 and iy0 <= iy1 and iz0 <= iz1:
                new_cubes[(ix0, ix1, iy0, iy1, iz0, iz1)] -= esgn

        if nsgn > 0:
            new_cubes[(nx0, nx1, ny0, ny1, nz0, nz1)] += nsgn

        cubes.update(new_cubes)

    return sum((x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1) * sgn
              for (x0, x1, y0, y1, z0, z1), sgn in cubes.items())

def get_reboots(lines: List[str], *, part2: bool) -> List[Reboot]:
    reboots: List[Reboot] = []

    for line in lines:
        on = line.startswith('on')
        numbers = tuple(map(int, re.findall(r'-?\d+', line)))

        if part2 or min(numbers) >= -50 and max(numbers) <= 50:
            reboots.append((on, numbers))
        
    return reboots


def main() -> int:
    lines = [line.strip() for line in sys.stdin]

    reboots1 = get_reboots(lines, part2=False)
    reboots2 = get_reboots(lines, part2=True)
    
    print(reactor_reboot(reboots1))
    print(reactor_reboot(reboots2))

if __name__ == '__main__':
    main()
