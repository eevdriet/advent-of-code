use std::{cmp::Ordering, collections::HashMap};

use once_cell::sync::Lazy;

use crate::{Gifts, TickerTape};

pub static ORDERINGS: Lazy<HashMap<&str, Ordering>> = Lazy::new(|| {
    HashMap::from([
        ("cats", Ordering::Greater),
        ("pomeranians", Ordering::Less),
        ("goldfish", Ordering::Less),
        ("trees", Ordering::Greater),
    ])
});

pub fn solve(
    tapes: &[TickerTape],
    gifts: &Gifts,
    orderings: &HashMap<&str, Ordering>,
) -> Vec<usize> {
    tapes
        .iter()
        .filter(|tape| {
            tape.gifts.iter().all(|(gift, gift_amount)| {
                // Determine how the gift amounts should be order
                let ord = orderings.get(gift).unwrap_or(&Ordering::Equal);
                let target_amount = gifts.get(gift);

                target_amount.is_some_and(|target_amount| gift_amount.cmp(target_amount) == *ord)
            })
        })
        .map(|tape| tape.id)
        .collect()
}
