use crate::{solve, state::State};

pub fn solve_part1(state: &State<2>) -> usize {
    solve(state)
}

#[cfg(test)]
mod tests {
    use aoc::io::File;

    use crate::parse::parse_initial_state1;

    use super::*;

    #[test]
    fn examples() {
        let example = File::Example(2021, 23).read().unwrap();
        let (_, state) = parse_initial_state1(&example).unwrap();

        assert_eq!(solve_part1(&state), 12_521);
    }

    #[test]
    fn input() {
        let input = File::Input(2021, 23).read().unwrap();
        let (_, state) = parse_initial_state1(&input).unwrap();

        assert_eq!(solve_part1(&state), 11_417);
    }
}
