use std::cmp::Ordering;

#[derive(PartialEq, Eq)]
pub struct Entry {
    pub encoded_state: u64,
    pub f_score: usize,
}

impl PartialOrd<Self> for Entry {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Entry {
    fn cmp(&self, other: &Self) -> Ordering {
        self.f_score.cmp(&other.f_score).reverse()
    }
}
