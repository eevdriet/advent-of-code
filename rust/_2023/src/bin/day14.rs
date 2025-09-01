use aoc::io::{read, File};
use std::{collections::HashSet, hash::Hasher};

// Part 1

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
struct Rocks {
    grid: Vec<Vec<char>>,
}

impl Rocks {
    fn parse(input: &str) -> Self {
        let grid = input
            .lines()
            .map(|line| line.chars().collect::<Vec<_>>())
            .collect::<Vec<_>>();
        Self { grid }
    }

    fn total_load(&self) -> usize {
        self.grid
            .iter()
            .enumerate()
            .map(|(y, row)| {
                row.iter()
                    .map(|ch| if *ch == 'O' { self.grid.len() - y } else { 0 })
                    .sum::<usize>()
            })
            .sum()
    }

    fn roll_north(&mut self, x: usize, y: usize) {
        for y in (1..=y).rev() {
            match self.grid[y - 1][x] {
                '#' | 'O' => break,
                _ => {
                    self.grid[y - 1][x] = 'O';
                    self.grid[y][x] = '.';
                }
            }
        }
    }
}

fn part1(rocks: &mut Rocks) -> usize {
    // Go through all possible rocks and roll them as far up north as possible
    for y in 0..rocks.grid.len() {
        for x in 0..rocks.grid[y].len() {
            if rocks.grid[y][x] == 'O' {
                rocks.roll_north(x, y);
            }
        }
    }

    rocks.total_load()
}

// Part 2

impl Rocks {
    fn roll_east(&mut self, x: usize, y: usize) {
        for x in x..self.grid[y].len() - 1 {
            match self.grid[y][x + 1] {
                '#' | 'O' => break,
                _ => {
                    self.grid[y][x + 1] = 'O';
                    self.grid[y][x] = '.';
                }
            }
        }
    }

    fn roll_south(&mut self, x: usize, y: usize) {
        for y in y..self.grid.len() - 1 {
            match self.grid[y + 1][x] {
                '#' | 'O' => break,
                _ => {
                    self.grid[y + 1][x] = 'O';
                    self.grid[y][x] = '.';
                }
            }
        }
    }

    fn roll_west(&mut self, x: usize, y: usize) {
        for x in (1..=x).rev() {
            match self.grid[y][x - 1] {
                '#' | 'O' => break,
                _ => {
                    self.grid[y][x - 1] = 'O';
                    self.grid[y][x] = '.';
                }
            }
        }
    }

    fn roll_all(&mut self) {
        // North and west need to scan from top left to bottom right
        for f in &[Self::roll_north, Self::roll_west] {
            for y in 0..self.grid.len() {
                for x in 0..self.grid[y].len() {
                    if self.grid[y][x] == 'O' {
                        f(self, x, y);
                    }
                }
            }
        }

        // For south and east, we need to scan in reverse
        for f in &[Self::roll_south, Self::roll_east] {
            for y in (0..self.grid.len()).rev() {
                for x in (0..self.grid[y].len()).rev() {
                    if self.grid[y][x] == 'O' {
                        f(self, x, y);
                    }
                }
            }
        }
    }
}

// Keep track of the grid from each iteration
#[derive(Debug, Eq)]
struct State {
    iter: usize,
    grid: Rocks,
}

impl State {
    fn new(step: usize, grid: Rocks) -> Self {
        Self { iter: step, grid }
    }
}

impl PartialEq for State {
    // Only the grid is relevant for a state, not the iteration when it was seen
    fn eq(&self, other: &Self) -> bool {
        self.grid == other.grid
    }
}

impl std::hash::Hash for State {
    fn hash<H: Hasher>(&self, state: &mut H) {
        self.grid.hash(state);
    }
}

fn part2(rocks: &mut Rocks) -> usize {
    // Keep track of which states were seen before to detect cycles
    let mut seen: HashSet<State> = HashSet::new();
    let n_iters = 1_000_000_000;

    for iter in 1..=n_iters {
        seen.insert(State::new(iter - 1, rocks.clone()));
        rocks.roll_all();

        // Cycle detected if state is seen before
        if let Some(old_state) = seen.get(&State::new(0, rocks.to_owned())) {
            // Determine cycle length and how many rolls are left in the cycle
            let cycle_len = iter - old_state.iter;
            let remaining = n_iters - iter;
            let remaining = remaining % cycle_len;

            // Complete cycle
            for _ in 0..remaining {
                rocks.roll_all();
            }

            return rocks.total_load();
        }
    }

    panic!("No cycles?");
}

fn main() {
    let txt = read(&File::Input(14)).unwrap();
    let mut rocks1 = Rocks::parse(&txt);
    let mut rocks2 = Rocks::parse(&txt);

    println!("Part 1: {}", part1(&mut rocks1));
    println!("Part 2: {}", part2(&mut rocks2));
}
