use nom::{IResult, character::complete};

pub fn parse_usize(input: &str) -> IResult<&str, usize> {
    let (input, num) = complete::u32(input)?;

    Ok((input, num as usize))
}
