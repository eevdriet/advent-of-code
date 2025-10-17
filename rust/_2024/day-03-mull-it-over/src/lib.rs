pub mod parse;
pub mod part1;
pub mod part2;

#[derive(Debug, Clone)]
pub enum Instruction {
    Mul(u32, u32),
    Do,
    Dont,
}
