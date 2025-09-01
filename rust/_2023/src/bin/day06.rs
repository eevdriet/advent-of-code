use aoc::io::{read, File};
use nom::{
    bytes::complete::tag,
    character::complete::{digit1, space1},
    multi::separated_list0,
    sequence::tuple,
    IResult,
};

struct Race {
    time: usize,
    distance: usize
}

impl Race {
    fn new(time: usize, distance: usize) -> Self {
        Self { time, distance }
    }

    fn winners(&self) -> usize {
        let mut winners = 0;

        for hold in 0..self.time {
            let distance = (self.time - hold) * hold;
            if distance > self.distance {
                winners += 1;
            }
        }

        return winners;
    }
}

fn part1(txt: &str) -> usize {
    fn parse(input: &str) -> IResult<&str, Vec<Race>> {
        let (input, (_, _, times, _)) = tuple((tag("Time:"), space1, separated_list0(space1, digit1), tag("\n")))(input)?;
        let (input, (_, _, distances)) = tuple((tag("Distance:"), space1, separated_list0(space1, digit1)))(input)?;

        Ok((input, times.iter().map(|t| t.parse::<usize>().unwrap()).zip(
                    distances.iter().map(|d| d.parse::<usize>().unwrap())
           ).map(|(time, distance)| Race::new(time, distance)).collect()))
    }

    let (_, races) = parse(txt).unwrap();
    races.iter().map(|r| r.winners()).product::<usize>()
}

fn part2(txt: &str) -> usize {
    fn parse(input: &str) -> IResult<&str, Race> {
        let (input, (_, time, _)) = tuple((tag("Time:"), digit1, tag("\n")))(&input[..])?;
        let (input, (_, distance)) = tuple((tag("Distance:"), digit1))(input)?;

        Ok((input, Race::new(time.parse::<usize>().unwrap(), distance.parse::<usize>().unwrap())))
    }

    let (_, race) = parse(txt).unwrap();
    race.winners()
}

fn main() {
    let txt1 = read(&File::Input(6)).unwrap();
    let txt2 = str::replace(&txt1, " ", "");

    println!("Part 1: {}", part1(&txt1));
    println!("Part 2: {}", part2(&txt2));
}
