use std::collections::{BinaryHeap, HashMap};

use crate::entry::Entry;
use crate::state::State;

pub mod parse;
pub mod part1;
pub mod part2;

pub mod amphipod;
pub mod entry;
pub mod state;

pub fn solve<const R: usize>(initial_state: &State<R>) -> usize {
    // Keep track of all states and their score towards reaching the goal
    let mut prio_queue = BinaryHeap::new();
    prio_queue.push(Entry {
        encoded_state: initial_state.encode(),
        f_score: 0,
    });

    let mut g_score: HashMap<u64, usize> = HashMap::new();
    g_score.insert(initial_state.encode(), 0);

    let encoded_goal_state = State::<R>::goal().encode();

    while let Some(Entry {
        encoded_state,
        f_score,
    }) = prio_queue.pop()
    {
        // Reached goal -> return the resulting cost of reaching it
        if encoded_state == encoded_goal_state {
            return f_score;
        }

        // Otherwise retrieve the state from its encoding
        let current_state = State::<R>::decode(encoded_state);
        let current_g_score = g_score[&encoded_state];

        for (next_state, transition_cost) in current_state.transitions() {
            let encoded_next_state = next_state.encode();

            let tentative_g_score = current_g_score + transition_cost;
            if tentative_g_score < *g_score.get(&encoded_next_state).unwrap_or(&usize::MAX) {
                g_score.insert(encoded_next_state, tentative_g_score);
                prio_queue.push(Entry {
                    encoded_state: encoded_next_state,
                    f_score: tentative_g_score + next_state.h_score(),
                });
            }
        }
    }

    unreachable!();
}
