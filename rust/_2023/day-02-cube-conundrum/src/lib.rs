use std::{cmp::max, collections::HashMap};

pub mod parse;
pub mod part1;
pub mod part2;

#[derive(Debug)]
pub struct Cube {
    color: String,
    amount: u32,
}

#[derive(Debug)]
pub struct Game {
    id: u32,
    rounds: Vec<Vec<Cube>>,
}

impl Game {
    pub fn is_possible(&self, bag: &HashMap<&str, u32>) -> bool {
        self.rounds.iter().all(|round| {
            round
                .iter()
                .all(|cube| cube.amount <= *bag.get(cube.color.as_str()).expect("valid color"))
        })
    }

    pub fn power(&self) -> u32 {
        self.rounds
            .iter()
            .flatten()
            .fold(
                HashMap::new(),
                |mut max_amounts: HashMap<&str, u32>, cube: &Cube| {
                    max_amounts
                        .entry(cube.color.as_str())
                        .and_modify(|amount| *amount = max(cube.amount, *amount))
                        .or_insert(cube.amount);

                    max_amounts
                },
            )
            .values()
            .product()
    }
}
