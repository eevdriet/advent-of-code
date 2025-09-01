use aoc::io::{read, File};

#[derive(Debug)]
struct Point {
    x: isize,
    y: isize,
}

impl Point {
    fn distance(&self, other: &Point) -> usize {
        let x = (self.x - other.x).abs();
        let y = (self.y - other.y).abs();

        (x + y) as usize
    }

    fn min(&self, other: &Point) -> Point {
        let x = self.x.min(other.x);
        let y = self.y.min(other.y);

        Point { x, y }
    }

    fn max(&self, other: &Point) -> Point {
        let x = self.x.max(other.x);
        let y = self.y.max(other.y);

        Point { x, y }
    }
}

fn expansions(
    stars: &[Point],
    empty_rows: &[isize],
    empty_cols: &[isize],
    n_expansions: usize,
) -> usize {
    let mut sum = 0;

    for (idx, star) in stars.iter().enumerate() {
        for other in &stars[idx + 1..] {
            let min = star.min(other);
            let max = star.max(other);

            let n_rows = empty_rows
                .iter()
                .filter(|row| min.y < **row && max.y > **row)
                .count()
                * n_expansions;
            let n_cols = empty_cols
                .iter()
                .filter(|cols| min.x < **cols && max.x > **cols)
                .count()
                * n_expansions;

            sum += star.distance(other) + n_rows + n_cols;
        }
    }

    sum
}

fn main() {
    let txt = read(&File::Input(11)).unwrap();
    let grid = txt
        .lines()
        .map(|line| line.chars().collect::<Vec<_>>())
        .collect::<Vec<_>>();

    let stars = grid
        .iter()
        .enumerate()
        .flat_map(|(y, row)| {
            row.iter()
                .enumerate()
                .filter(|(_, col)| **col == '#')
                .map(move |(x, _)| Point {
                    x: x as isize,
                    y: y as isize,
                })
        })
        .collect::<Vec<_>>();

    let empty_rows = grid
        .iter()
        .enumerate()
        .filter(|(_, row)| row.iter().all(|col| *col == '.'))
        .map(|(y, _)| y as isize)
        .collect::<Vec<_>>();

    let empty_cols = (0..grid[0].len())
        .filter(|x| grid.iter().all(|row| row[*x] == '.'))
        .map(|x| x as isize)
        .collect::<Vec<_>>();

    println!(
        "Part 1: {}",
        expansions(&stars, &empty_rows, &empty_cols, 1)
    );
    println!(
        "Part 2: {}",
        expansions(&stars, &empty_rows, &empty_cols, 999_999)
    );
}
