use std::collections::HashMap;

use aoc::io::{read, File};
use nom::{
    bytes::complete::tag,
    character::complete::{digit1, newline, one_of, space1},
    multi::{many1, separated_list1},
    IResult,
};

#[derive(Debug, PartialEq, Eq, Clone, Hash)]
enum Spring {
    Operational, // '#'
    Damaged,     // '.'
    Unknown,     // '?'
}

impl From<char> for Spring {
    fn from(ch: char) -> Self {
        match ch {
            '.' => Spring::Operational,
            '#' => Spring::Damaged,
            _ => Spring::Unknown,
        }
    }
}

#[derive(Debug, Eq, PartialEq, Clone, Hash)]
struct Record {
    springs: Vec<Spring>,
    groups: Vec<usize>,
}

impl Record {
    fn parse(input: &str) -> IResult<&str, Self> {
        let (input, springs) = many1(one_of(".#?"))(input)?;
        let (input, _) = space1(input)?;
        let (input, groups) = separated_list1(tag(","), digit1)(input)?;

        Ok((
            input,
            Self {
                springs: springs.into_iter().map(|ch| ch.into()).collect(),
                groups: groups.into_iter().map(|g| g.parse().unwrap()).collect(),
            },
        ))
    }

    fn parse_all(input: &str) -> Vec<Self> {
        separated_list1(newline, Record::parse)(input).unwrap().1
    }

    fn unfold(&self) -> Record {
        let springs = self
            .springs
            .iter()
            .cloned()
            .chain([Spring::Unknown].iter().cloned())
            .cycle()
            .take(5 * self.springs.len() + 4)
            .collect();

        let groups = self
            .groups
            .iter()
            .cloned()
            .cycle()
            .take(5 * self.groups.len())
            .collect();

        Record { springs, groups }
    }
}

fn count_solutions(dp: &mut HashMap<Record, usize>, record: &Record) -> usize {
    // Existing solution
    if let Some(&count) = dp.get(record) {
        return count;
    }

    // No more groups left; complete solution
    if record.groups.is_empty() {
        // Verify whether there are any damaged springs left
        let count = 1 - record.springs.iter().any(|s| *s == Spring::Damaged) as usize;

        dp.insert(record.clone(), count);
        return count;
    }

    // Not enough spaces to fill the groups
    let n_unknown = record.groups.iter().sum::<usize>() + record.groups.len() - 1;
    if record.springs.len() < n_unknown {
        let count = 0;

        dp.insert(record.clone(), count);
        return count;
    }

    // Skip starting operational spring
    if record.springs[0] == Spring::Operational {
        let new_record = Record {
            springs: record.springs[1..].to_vec(),
            groups: record.groups.clone(),
        };
        let count = count_solutions(dp, &new_record);

        dp.insert(record.clone(), count);
        return count;
    }

    let mut count = 0;
    let curr = record.groups[0];
    let end = (curr + 1).min(record.springs.len());

    let all_non_operational = record.springs[0..curr]
        .iter()
        .all(|spring| *spring != Spring::Operational);
    let no_first = (record.springs.len() > curr && record.springs[curr] != Spring::Damaged)
        || record.springs.len() <= curr;

    if all_non_operational && no_first {
        let new_record = Record {
            springs: record.springs[end..].to_vec(),
            groups: record.groups[1..].to_vec(),
        };

        count = count_solutions(dp, &new_record);
    }

    if record.springs[0] == Spring::Unknown {
        let new_record = Record {
            springs: record.springs[1..].to_vec(),
            groups: record.groups.clone(),
        };

        count += count_solutions(dp, &new_record);
    }

    dp.insert(record.clone(), count);
    return count;
}

fn part1(records: &Vec<Record>) -> usize {
    let mut dp: HashMap<Record, usize> = HashMap::new();

    records
        .iter()
        .map(|record| count_solutions(&mut dp, record))
        .sum::<usize>()
}

fn part2(records: &Vec<Record>) -> usize {
    let mut dp: HashMap<Record, usize> = HashMap::new();

    records
        .iter()
        .map(|record| count_solutions(&mut dp, &record.unfold()))
        .sum::<usize>()
}

fn main() {
    let txt = read(&File::Input(12)).unwrap();
    let records = Record::parse_all(&txt);

    println!("Part 1: {}", part1(&records));
    println!("Part 2: {}", part2(&records));
}
