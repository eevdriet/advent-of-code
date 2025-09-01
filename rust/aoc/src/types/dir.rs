use std::ops::Add;

#[derive(Clone, Copy)]
pub enum Direction {
    North,
    East,
    South,
    West,
}

impl Into<(isize, isize)> for Direction {
    fn into(self) -> (isize, isize) {
        match self {
            Direction::North => (-1, 0),
            Direction::East => (0, 1),
            Direction::South => (1, 0),
            Direction::West => (0, -1),
        }
    }
}

impl TryFrom<char> for Direction {
    type Error = ();

    fn try_from(value: char) -> Result<Self, Self::Error> {
        match value {
            '^' | 'N' => Ok(Direction::North),
            '>' | 'E' => Ok(Direction::East),
            'v' | 'S' => Ok(Direction::South),
            '<' | 'W' => Ok(Direction::West),
            _ => Err(()),
        }
    }
}

impl Add<Direction> for (isize, isize) {
    type Output = (isize, isize);

    fn add(self, dir: Direction) -> Self::Output {
        match dir {
            Direction::North => (self.0 - 1, self.1),
            Direction::East => (self.0, self.1 + 1),
            Direction::South => (self.0 + 1, self.1),
            Direction::West => (self.0, self.1 - 1),
        }
    }
}
