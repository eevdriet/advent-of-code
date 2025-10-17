use nom::{
    IResult, Parser,
    branch::alt,
    bytes::complete::tag,
    character::complete::{self, anychar, char},
    combinator::value,
    multi::{many_till, many1},
    sequence::{delimited, separated_pair},
};

use crate::Instruction;

fn parse_mul(input: &str) -> IResult<&str, Instruction> {
    let (input, _) = tag("mul")(input)?;
    let (input, pair) = delimited(
        char('('),
        separated_pair(complete::u32, char(','), complete::u32),
        char(')'),
    )(input)?;

    Ok((input, Instruction::Mul(pair.0, pair.1)))
}

fn parse_instruction(input: &str) -> IResult<&str, Instruction> {
    alt((
        value(Instruction::Do, tag("do()")),
        value(Instruction::Dont, tag("don't()")),
        parse_mul,
    ))(input)
}

pub fn parse_instructions(input: &str) -> IResult<&str, Vec<Instruction>> {
    many1(many_till(anychar, parse_instruction).map(|(_, instruction)| instruction))(input)
}
