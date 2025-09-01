use aoc::parse::parse_usize;
use nom::{
    IResult,
    branch::alt,
    bytes::complete::tag,
    character::complete::{char, newline, space1},
    multi::separated_list0,
    sequence::{separated_pair, terminated},
};

use crate::{Instruction, SwitchType};

pub fn parse_coord(input: &str) -> IResult<&str, (usize, usize)> {
    separated_pair(parse_usize, char(','), parse_usize)(input)
}

pub fn parse_instruction(input: &str) -> IResult<&str, Instruction> {
    let (input, switch_type) = terminated(
        alt((tag("turn off"), tag("turn on"), tag("toggle"))),
        space1,
    )(input)?;

    let switch = match switch_type {
        "turn off" => SwitchType::Off,
        "turn on" => SwitchType::On,
        "toggle" => SwitchType::Toggle,
        _ => panic!("Should not occur"),
    };

    let (input, (start, end)) = separated_pair(parse_coord, tag(" through "), parse_coord)(input)?;

    let instruction = Instruction { switch, start, end };
    Ok((input, instruction))
}

pub fn parse_instructions(input: &str) -> IResult<&str, Vec<Instruction>> {
    separated_list0(newline, parse_instruction)(input)
}
