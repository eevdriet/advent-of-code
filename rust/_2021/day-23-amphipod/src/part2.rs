use crate::{solve, state::State};

pub fn solve_part2(state: &State<4>) -> usize {
    solve(state)
}

#[cfg(test)]
mod tests {
    use aoc::io::File;

    use crate::parse::parse_initial_state2;

    use super::*;

    #[test]
    fn examples() {
        let example = File::Example(2021, 23).read().unwrap();
        let (_, state) = parse_initial_state2(&example).unwrap();

        assert_eq!(solve_part2(&state), 44_169);
    }

    #[test]
    fn input() {
        let input = File::Input(2021, 23).read().unwrap();
        let (_, state) = parse_initial_state2(&input).unwrap();

        assert_eq!(solve_part2(&state), 49_529);
    }
}
