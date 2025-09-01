use nom::IResult;

pub fn parse_input(input: &str) -> IResult<&str, Option<i32>> {
    Ok((input, None))
}
