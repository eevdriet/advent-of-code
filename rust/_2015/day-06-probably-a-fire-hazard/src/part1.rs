use std::collections::HashMap;

use crate::{Instruction, SwitchType};

pub fn solve(instructions: &[Instruction]) -> usize {
    instructions
        .iter()
        .fold(HashMap::new(), |mut turned_lights, instruction| {
            let (x1, y1) = instruction.start;
            let (x2, y2) = instruction.end;

            let (xmin, xmax) = (x1.min(x2), x1.max(x2));
            let (ymin, ymax) = (y1.min(y2), y1.max(y2));

            for x in xmin..=xmax {
                for y in ymin..=ymax {
                    let pos = (x, y);

                    let entry = turned_lights.entry(pos).or_insert(false);
                    *entry = match instruction.switch {
                        SwitchType::On => true,
                        SwitchType::Off => false,
                        SwitchType::Toggle => !*entry,
                    }
                }
            }

            turned_lights
        })
        .values()
        .filter(|is_turned| **is_turned)
        .count()
}
