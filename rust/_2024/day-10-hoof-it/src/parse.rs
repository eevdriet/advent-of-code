use nom::{
    IResult, bytes::complete::take_while1, character::complete::newline, multi::separated_list1,
};

fn parse_row(input: &str) -> IResult<&str, Vec<u8>> {
    let (input, digits) = take_while1(|ch: char| ch.is_ascii_digit())(input)?;
    let row = digits.chars().map(|ch| ch as u8 - b'0').collect();

    Ok((input, row))
}

pub fn parse_grid(input: &str) -> IResult<&str, Vec<Vec<u8>>> {
    separated_list1(newline, parse_row)(input)
}
