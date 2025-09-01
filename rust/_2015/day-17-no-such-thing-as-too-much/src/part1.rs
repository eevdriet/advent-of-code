use crate::Containers;

pub fn solve(containers: &Containers, capacity: usize) -> usize {
    // Track in how many ways each amount up to the capacity can be made
    let mut dp = vec![0; capacity + 1];
    dp[0] = 1;

    // Try all amounts for all containers that are valid
    for &container in containers {
        for amount in (container..=capacity).rev() {
            dp[amount] += dp[amount - container];
        }
    }

    dp[capacity]
}
