use std::collections::HashMap;

use crate::Game;

pub fn solve(games: &[Game]) -> u32 {
    let bag = HashMap::from([("red", 12), ("green", 13), ("blue", 14)]);

    games
        .iter()
        .filter(|game| game.is_possible(&bag))
        .map(|game| game.id)
        .sum::<u32>()
}
