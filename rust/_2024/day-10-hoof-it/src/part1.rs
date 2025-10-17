use std::collections::HashSet;

pub fn solve(height_map: &[Vec<u8>]) -> usize {
    // Determine all 0-height indices
    let trail_heads = height_map
        .iter()
        .enumerate()
        .flat_map(|(r, row)| {
            row.iter()
                .enumerate()
                .filter(|(_, h)| **h == 0)
                .map(move |(c, _)| (r, c))
        })
        .collect::<Vec<_>>();

    // DFS to count all 9-height trail endings
    fn dfs(
        row: usize,
        col: usize,
        height_map: &[Vec<u8>],
        visited: &mut HashSet<(usize, usize)>,
    ) -> usize {
        // Visited position before -> no new ending can be reached
        if visited.contains(&(row, col)) {
            return 0;
        }
        visited.insert((row, col));

        // Determine the current height and whether we are at a trail ending
        let height = height_map[row][col];
        if height == 9 {
            return 1;
        }

        // If not, go to all valid neighboring positions and recursively count endings
        let mut n_peaks = 0;
        let directions = [(0isize, 1isize), (1, 0), (0, -1), (-1, 0)];

        for (dr, dc) in directions {
            let nr = row as isize + dr;
            let nc = col as isize + dc;

            if nr < 0 || nc < 0 {
                continue;
            }

            let nr = nr as usize;
            let nc = nc as usize;

            if nr < height_map.len()
                && nc < height_map[nr].len()
                && height_map[nr][nc] == height + 1
            {
                n_peaks += dfs(nr, nc, height_map, visited);
            }
        }

        n_peaks
    }

    trail_heads
        .iter()
        .map(|&(r, c)| {
            let mut visited = HashSet::new();
            dfs(r, c, height_map, &mut visited)
        })
        .sum()
}

#[cfg(test)]
mod tests {
    use aoc::io::File;

    use crate::parse::parse_grid;

    use super::*;

    #[test]
    fn examples() {
        let example = File::Example(2024, 10).read().unwrap();
        let (_, grid) = parse_grid(&example).unwrap();

        assert_eq!(solve(&grid), 36);
    }

    #[test]
    fn input() {
        let input = File::Input(2024, 10).read().unwrap();
        let (_, grid) = parse_grid(&input).unwrap();

        assert_eq!(solve(&grid), 607);
    }
}
