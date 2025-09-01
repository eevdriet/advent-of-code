use anyhow::Result;
use aoc::io::{read_one_per_line, File};
use std::str::FromStr;

#[derive(Debug)]
enum Direction {
    Forward(u32),
    Down(u32),
    Up(u32),
}

impl FromStr for Direction {
    type Err = anyhow::Error;

    fn from_str(s: &str) -> Result<Self> {
        if let Some((direction, distance)) = s.split_once(" ") {
            let distance = distance.parse()?;

            Ok(match direction {
                "forward" => Direction::Forward(distance),
                "down" => Direction::Down(distance),
                "up" => Direction::Up(distance),
                _ => panic!("Unhandled direction"),
            })
        } else {
            Err(anyhow::format_err!("could not split direction"))
        }
    }
}

#[derive(Debug, Default)]
struct Location {
    distance: u32,
    depth: u32,

    // Part 2, can ignore for part 1
    aim: u32,
}

impl Location {
    fn answer(&self) -> u32 {
        self.distance * self.depth
    }
}

fn part1() -> Result<u32> {
    Ok(read_one_per_line(&File::Input(2))?
        .iter()
        .fold(Location::default(), |loc, dir| match dir {
            Direction::Forward(distance) => Location {
                distance: loc.distance + distance,
                ..loc
            },
            Direction::Up(distance) => Location {
                depth: loc.depth - distance,
                ..loc
            },
            Direction::Down(distance) => Location {
                depth: loc.depth + distance,
                ..loc
            },
        })
        .answer())
}

fn part2() -> Result<u32> {
    Ok(read_one_per_line(&File::Input(2))?
        .iter()
        .fold(Location::default(), |loc, dir| match dir {
            Direction::Forward(distance) => Location {
                distance: loc.distance + distance,
                depth: loc.depth + distance * loc.aim,
                ..loc
            },
            Direction::Up(aim) => Location {
                aim: loc.aim - aim,
                ..loc
            },
            Direction::Down(aim) => Location {
                aim: loc.aim + aim,
                ..loc
            },
        })
        .answer())
}

fn main() {
    if let Ok(ans) = part1() {
        println!("Part 1: {ans}")
    }

    if let Ok(ans) = part2() {
        println!("Part 2: {ans}");
    }
}
