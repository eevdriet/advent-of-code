use aoc::types::Direction;

use nom::{IResult, character::complete::anychar, combinator::map_res, multi::many0};

pub fn parse_direction(input: &str) -> IResult<&str, Direction> {
    map_res(anychar, Direction::try_from)(input)
}

pub fn parse_directions(input: &str) -> IResult<&str, Vec<Direction>> {
    many0(parse_direction)(input)
}
