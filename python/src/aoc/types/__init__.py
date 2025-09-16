from collections import namedtuple
from typing import Literal

Coord2D = namedtuple("Coord2D", ["x", "y"])
Coord3D = namedtuple("Coord3D", ["x", "y", "z"])

LetterDirection = Literal["U"] | Literal["D"] | Literal["L"] | Literal["R"]
