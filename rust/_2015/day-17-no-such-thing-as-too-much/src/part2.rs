use std::cmp::Ordering;

use crate::Containers;

pub fn solve(containers: &Containers, capacity: usize) -> usize {
    // Track in how many ways each amount up to the capacity can be made
    // Additionally track the smallest number of containers that achieves this
    let mut dp = vec![(usize::MAX, 0); capacity + 1];
    dp[0] = (0, 1);

    // Try all amounts for all containers that are valid
    for &container in containers {
        // iterate backwards to avoid double-counting the same container
        for amount in (container..=capacity).rev() {
            let (prev_min, prev_ways) = dp[amount - container];

            // If we can do it with fewer containers than before, update this as well
            if let Some(candidate_min) = prev_min.checked_add(1) {
                match dp[amount].0.cmp(&candidate_min) {
                    // Found a better (smaller) container count
                    Ordering::Greater => {
                        dp[amount] = (candidate_min, prev_ways);
                    }

                    // Uses same amount of containers, so add the number of ways
                    Ordering::Equal => {
                        dp[amount].1 += prev_ways;
                    }

                    // Worse number of ways: do nothing
                    Ordering::Less => {}
                }
            }
        }
    }

    dp[capacity].1
}
