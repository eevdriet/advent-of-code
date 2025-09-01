use nom::{
    IResult,
    branch::alt,
    bytes::complete::tag,
    character::complete::{self, newline},
    multi::{separated_list0, separated_list1},
    sequence::{delimited, preceded},
};

use crate::TickerTape;

pub fn parse_gift(input: &str) -> IResult<&str, (&str, usize)> {
    let (input, gift) = alt((
        tag("children"),
        tag("cats"),
        tag("samoyeds"),
        tag("pomeranians"),
        tag("akitas"),
        tag("vizslas"),
        tag("goldfish"),
        tag("trees"),
        tag("cars"),
        tag("perfumes"),
    ))(input)?;
    let (input, amount) = preceded(tag(": "), complete::u32)(input)?;

    Ok((input, (gift, amount as usize)))
}

pub fn parse_tape(input: &str) -> IResult<&str, TickerTape> {
    // Initialize the tape from its identifier
    let (input, id) = delimited(tag("Sue "), complete::u32, tag(": "))(input)?;

    let mut tape = TickerTape {
        id: id as usize,
        ..Default::default()
    };

    // Then parse its fields
    let (input, gifts) = separated_list0(tag(", "), parse_gift)(input)?;
    for (gift, amount) in gifts {
        tape.gifts.insert(gift, amount);
    }

    Ok((input, tape))
}

pub fn parse_tapes(input: &str) -> IResult<&str, Vec<TickerTape>> {
    separated_list1(newline, parse_tape)(input)
}
