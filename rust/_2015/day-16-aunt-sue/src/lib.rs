use once_cell::sync::Lazy;
use std::collections::HashMap;

pub mod parse;
pub mod part1;
pub mod part2;

pub type Gifts<'a> = HashMap<&'a str, usize>;

#[derive(Debug, Default)]
pub struct TickerTape<'a> {
    id: usize,
    gifts: Gifts<'a>,
}

pub static GIFTS: Lazy<Gifts> = Lazy::new(|| {
    HashMap::from([
        ("children", 3),
        ("cats", 7),
        ("samoyeds", 2),
        ("pomeranians", 3),
        ("akitas", 0),
        ("vizslas", 0),
        ("goldfish", 5),
        ("trees", 3),
        ("cars", 2),
        ("perfumes", 1),
    ])
});
