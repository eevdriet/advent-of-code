use nom::{
    IResult,
    bytes::complete::tag,
    character::complete::{self, alpha1, char, line_ending},
    multi::separated_list1,
    sequence::{preceded, separated_pair},
};

use crate::{Cube, Game};

fn parse_cubes(input: &str) -> IResult<&str, Cube> {
    let (input, (amount, color)) = separated_pair(complete::u32, char(' '), alpha1)(input)?;

    Ok((
        input,
        Cube {
            amount,
            color: color.to_string(),
        },
    ))
}

fn parse_round(input: &str) -> IResult<&str, Vec<Cube>> {
    separated_list1(tag(", "), parse_cubes)(input)
}

fn parse_game(input: &str) -> IResult<&str, Game> {
    let (input, id) = preceded(tag("Game "), complete::u32)(input)?;
    let (input, rounds) = preceded(tag(": "), separated_list1(tag("; "), parse_round))(input)?;

    Ok((input, Game { id, rounds }))
}

pub fn parse_games(input: &str) -> IResult<&str, Vec<Game>> {
    separated_list1(line_ending, parse_game)(input)
}
