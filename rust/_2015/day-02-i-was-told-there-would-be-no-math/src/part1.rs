use crate::Gift;

pub fn solve(gifts: &[Gift]) -> usize {
    gifts.iter().map(|gift| gift.wrapping_required()).sum()
}
