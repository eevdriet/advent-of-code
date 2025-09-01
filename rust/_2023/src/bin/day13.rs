use aoc::io::{read, File};

struct Note {
    grid: Vec<Vec<char>>,
}

impl From<&str> for Note {
    fn from(note_str: &str) -> Self {
        let grid = note_str
            .lines()
            .map(|line| line.chars().collect())
            .collect();

        Self { grid }
    }
}

// Part 1
impl Note {
    fn rows_equal(&self, y1: usize, y2: usize) -> bool {
        self.grid[y1] == self.grid[y2]
    }

    fn cols_equal(&self, x1: usize, x2: usize) -> bool {
        for y in 0..self.grid.len() {
            if self.grid[y][x1] != self.grid[y][x2] {
                return false;
            }
        }

        return true;
    }

    fn reflect1(&self) -> usize {
        // Try to find a reflection along the rows
        'rows: for y in 0..self.grid.len() - 1 {
            if !self.rows_equal(y, y + 1) {
                continue 'rows;
            }

            // If found, determine minimum distance to side edges and check the rest
            let min_dist = y.min(self.grid.len() - y - 2);
            for dist in 1..=min_dist {
                if !self.rows_equal(y - dist, y + 1 + dist) {
                    continue 'rows;
                }
            }

            return 100 * (y + 1);
        }

        // Try to find a reflection along the columns
        'cols: for x in 0..self.grid[0].len() - 1 {
            if !self.cols_equal(x, x + 1) {
                continue 'cols;
            }

            // If found, determine minimum distance to top and bottom edges and check the rest
            let min_dist = x.min(self.grid[0].len() - x - 2);
            for dist in 1..=min_dist {
                if !self.cols_equal(x - dist, x + 1 + dist) {
                    continue 'cols;
                }
            }

            return x + 1;
        }

        0
    }
}

// Part 2
impl Note {
    fn rows_diff(&self, y1: usize, y2: usize) -> usize {
        let mut diff = 0;

        for x in 0..self.grid[0].len() {
            if self.grid[y1][x] != self.grid[y2][x] {
                diff += 1;
            }
        }

        diff
    }

    fn cols_diff(&self, x1: usize, x2: usize) -> usize {
        let mut diff = 0;

        for y in 0..self.grid.len() {
            if self.grid[y][x1] != self.grid[y][x2] {
                diff += 1;
            }
        }

        diff
    }

    fn reflect2(&self) -> usize {
        // Try to find a reflection along the rows
        'rows: for y in 0..self.grid.len() - 1 {
            // At most one smudge allowed along the reflection
            let mut n_smudges = self.rows_diff(y, y + 1);
            if n_smudges > 1 {
                continue 'rows;
            }

            // If so, count the remaining number of smudges
            let min_dist = y.min(self.grid.len() - y - 2);
            for dist in 1..=min_dist {
                n_smudges += self.rows_diff(y - dist, y + 1 + dist);
                if n_smudges > 1 {
                    continue 'rows;
                }
            }

            // Exactly one smudge needed for reflection, otherwise continue looking
            if n_smudges == 0 {
                continue 'rows;
            }

            return 100 * (y + 1);
        }

        // Try to find a reflection along the columns
        'cols: for x in 0..self.grid[0].len() - 1 {
            // At most one smudge allowed along the reflection
            let mut n_smudges = self.cols_diff(x, x + 1);
            if n_smudges > 1 {
                continue 'cols;
            }

            // If so, count the remaining number of smudges
            let min_dist = x.min(self.grid[0].len() - x - 2);
            for dist in 1..=min_dist {
                n_smudges += self.cols_diff(x - dist, x + 1 + dist);
                if n_smudges > 1 {
                    continue 'cols;
                }
            }

            // Exactly one smudge needed for reflection, otherwise continue looking
            if n_smudges == 0 {
                continue 'cols;
            }

            return x + 1;
        }

        0
    }
}

fn main() {
    let txt = read(&File::Input(13)).unwrap();
    let notes = txt
        .split("\n\n")
        .map(|note| note.into())
        .collect::<Vec<Note>>();

    let p1 = notes.iter().map(|note| note.reflect1()).sum::<usize>();
    println!("Part 1: {}", p1);

    let p2 = notes.iter().map(|note| note.reflect2()).sum::<usize>();
    println!("Part 2: {}", p2);
}
