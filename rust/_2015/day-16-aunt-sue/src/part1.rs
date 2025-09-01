use crate::{Gifts, TickerTape};

pub fn solve(tapes: &[TickerTape], gifts: &Gifts) -> Vec<usize> {
    tapes
        .iter()
        .filter(|tape| {
            tape.gifts
                .iter()
                .all(|(gift, amount)| gifts.get(gift) == Some(amount))
        })
        .map(|tape| tape.id)
        .collect()
}
