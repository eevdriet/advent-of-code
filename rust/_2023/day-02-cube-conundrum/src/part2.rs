use crate::Game;

pub fn solve(games: &[Game]) -> u32 {
    games.iter().map(|game| game.power()).sum::<u32>()
}
