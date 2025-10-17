use crate::Instruction;

pub fn solve(instructions: &[Instruction]) -> u32 {
    let (_, sum) =
        instructions.iter().fold(
            (true, 0),
            |(should_do, sum), instruction| match instruction {
                Instruction::Mul(left, right) => {
                    if should_do {
                        (should_do, sum + left * right)
                    } else {
                        (should_do, sum)
                    }
                }
                Instruction::Do => (true, sum),
                Instruction::Dont => (false, sum),
            },
        );

    sum
}

#[cfg(test)]
mod tests {
    use aoc::io::File;

    use crate::parse::parse_instructions;

    use super::*;

    #[test]
    fn examples() {
        let example = File::ExampleN(2024, 3, 2).read().unwrap();
        let (_, state) = parse_instructions(&example).unwrap();

        assert_eq!(solve(&state), 48);
    }

    #[test]
    fn input() {
        let input = File::Input(2024, 3).read().unwrap();
        let (_, instructions) = parse_instructions(&input).unwrap();

        assert_eq!(solve(&instructions), 88_811_886);
    }
}
