use std::collections::HashSet;

use aoc::types::Direction;

pub fn solve(directions: &[Direction]) -> usize {
    directions
        .iter()
        .enumerate()
        .scan(((0, 0), (0, 0)), |(santa, robo), (i, dir)| {
            // Move with Santa
            if i % 2 == 0 {
                *santa = *santa + *dir;
                Some(*santa)
            }
            // Move with Robo Santa
            else {
                *robo = *robo + *dir;
                Some(*robo)
            }
        })
        .fold(HashSet::from([(0, 0)]), |mut visited, pos| {
            visited.insert(pos);
            visited
        })
        .len()
}
