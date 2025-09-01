use aoc::types::Direction;
use std::collections::HashSet;

pub fn solve(directions: &[Direction]) -> usize {
    directions
        .iter()
        .scan((0, 0), |pos, dir| {
            *pos = *pos + *dir;
            Some(*pos)
        })
        .fold(HashSet::from([(0, 0)]), |mut visited, pos| {
            visited.insert(pos);
            visited
        })
        .len()
}
