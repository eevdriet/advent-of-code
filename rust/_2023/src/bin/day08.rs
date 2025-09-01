use aoc::io::{read, File};
use std::collections::HashMap;

#[derive(Debug)]
struct Edges<'a> {
    left: &'a str,
    right: &'a str,
}

#[derive(Debug)]
enum Direction {
    Left,
    Right,
}

impl Direction {
    fn new(ch: char) -> Self {
        match ch {
            'L' => Direction::Left,
            _ => Direction::Right,
        }
    }
}

#[derive(Debug)]
struct Map<'a> {
    directions: Vec<Direction>,
    edges: HashMap<&'a str, Edges<'a>>,
}

impl Map<'_> {
    fn parse(input: &str) -> Map {
        let (directions, mappings) = input.split_once("\n\n").unwrap();
        let directions = directions.chars().map(|ch| Direction::new(ch)).collect();

        let mut edges: HashMap<&str, Edges> = HashMap::new();
        for line in mappings.lines() {
            let (src, lr) = line.split_once(" = (").unwrap();
            let (left, right) = lr.split_once(", ").unwrap();
            let right = &right[..3];

            edges.insert(src, Edges { left, right });
        }

        Map { directions, edges }
    }

    fn find_end<'a, F>(&'a self, start: &'a str, end: F) -> (usize, &str)
    where
        F: Fn(&str) -> bool,
    {
        let mut step = 0;
        let mut curr = start;

        for dir in self.directions.iter().cycle() {
            let edges = self.edges.get(curr).unwrap();
            curr = match dir {
                Direction::Left => edges.left,
                Direction::Right => edges.right,
            };

            step += 1;
            if end(curr) {
                break;
            }
        }

        (step, curr)
    }
}

fn part1(map: &Map) -> usize {
    map.find_end("AAA", |node| node == "ZZZ").0
}

fn part2(map: &Map) -> usize {
    // Determine which nodes to start/end from
    let starts = map
        .edges
        .keys()
        .filter(|k| k.ends_with('A'))
        .collect::<Vec<_>>();
    let ends = map
        .edges
        .keys()
        .filter(|k| k.ends_with('Z'))
        .collect::<Vec<_>>();

    // Determine how many steps each start -> end requires
    let mut steps: Vec<usize> = Vec::new();
    for start in starts {
        let (step, _) = map.find_end(start, |node| ends.contains(&&node));
        steps.push(step);
    }

    // Find LCM of all steps for the answer
    fn lcm(nums: &[usize]) -> usize {
        if nums.len() == 1 {
            return nums[0];
        }

        let a = nums[0];
        let b = lcm(&nums[1..]);
        a * b / gcd(a, b)
    }

    fn gcd(a: usize, b: usize) -> usize {
        if b == 0 {
            return a;
        }

        gcd(b, a % b)
    }

    return lcm(&steps);
}

fn main() {
    let txt = read(&File::Input(8)).unwrap();
    let map = Map::parse(&txt);

    println!("Part 1: {}", part1(&map));
    println!("Part 2: {}", part2(&map));
}
