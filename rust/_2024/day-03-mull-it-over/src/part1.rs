use crate::Instruction;

pub fn solve(instructions: &[Instruction]) -> u32 {
    instructions
        .iter()
        .map(|instruction| match instruction {
            Instruction::Mul(left, right) => left * right,
            _ => 0,
        })
        .sum()
}

#[cfg(test)]
mod tests {
    use aoc::io::File;

    use crate::parse::parse_instructions;

    use super::*;

    #[test]
    fn examples() {
        let example = File::ExampleN(2024, 3, 1).read().unwrap();
        let (_, instructions) = parse_instructions(&example).unwrap();

        assert_eq!(solve(&instructions), 161);
    }

    #[test]
    fn input() {
        let input = File::Input(2024, 3).read().unwrap();
        let (_, instructions) = parse_instructions(&input).unwrap();

        assert_eq!(solve(&instructions), 166_357_705);
    }
}
