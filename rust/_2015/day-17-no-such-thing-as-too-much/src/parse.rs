use aoc::parse::parse_usize;
use nom::{IResult, character::complete::newline, multi::separated_list1};

use crate::Containers;

pub fn parse_containers(input: &str) -> IResult<&str, Containers> {
    separated_list1(newline, parse_usize)(input)
}
