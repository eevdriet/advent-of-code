use aoc::parse::parse_usize;
use nom::{
    IResult, bytes::complete::tag, character::complete::newline, multi::separated_list1,
    sequence::tuple,
};

use crate::Gift;

pub fn parse_gift(input: &str) -> IResult<&str, Gift> {
    let (input, (length, _, width, _, height)) =
        tuple((parse_usize, tag("x"), parse_usize, tag("x"), parse_usize))(input)?;

    Ok((
        input,
        Gift {
            length,
            width,
            height,
        },
    ))
}

pub fn parse_gifts(input: &str) -> IResult<&str, Vec<Gift>> {
    separated_list1(newline, parse_gift)(input)
}
