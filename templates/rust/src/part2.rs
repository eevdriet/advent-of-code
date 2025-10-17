pub fn solve(data: &i32) -> i32 {
    *data
}

#[cfg(test)]
mod tests {
    use aoc::io::File;

    use crate::parse::parse_input;

    use super::*;

    #[test]
    fn examples() {
        let example = File::Example({{year}}, {{day}}).read().unwrap();
        let (_, data) = parse_input(&example).unwrap();

        assert_eq!(solve(&data), 0);
    }

    #[test]
    fn input() {
        let input = File::Input({{year}}, {{day}}).read().unwrap();
        let (_, data) = parse_input(&input).unwrap();

        assert_eq!(solve(&data), 0);
    }
}
