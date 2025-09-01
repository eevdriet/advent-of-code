use crate::Gift;

pub fn solve(gifts: &[Gift]) -> usize {
    gifts.iter().map(|gift| gift.ribbon_required()).sum()
}
