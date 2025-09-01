pub mod parse;
pub mod part1;
pub mod part2;

enum SwitchType {
    On,
    Off,
    Toggle,
}

pub struct Instruction {
    switch: SwitchType,
    start: (usize, usize),
    end: (usize, usize),
}
