use std::{collections::HashSet, ops::Sub};

pub fn solve(words: &[&str]) -> usize {
    words
        .iter()
        .filter(|word| {
            // Verify whether a consecutive letter pair appears multiple times without overlap
            let has_pair_twice = {
                let mut seen = HashSet::new();
                let mut found = false;

                for idx in 0..word.len().sub(1) {
                    let pair = &word[idx..idx + 2];

                    if seen.contains(&pair) {
                        found = true;
                        break;
                    }

                    seen.insert(pair);

                    // Remove overlapping pairs so only non-overlapping count
                    if idx >= 1 {
                        seen.remove(&word[idx - 1..idx + 1]);
                    }
                }

                found
            };

            // Verify if two characters with gap inbetween are the same, i.e. repeating
            let has_skip_repeat = word
                .chars()
                .zip(word.chars().skip(2))
                .any(|(first, second)| first == second);

            has_pair_twice && has_skip_repeat
        })
        .count()
}
