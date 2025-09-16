use nom::IResult;

use crate::{amphipod::Amphipod, state::State};

pub fn parse_amphipods(input: &str) -> Vec<Amphipod> {
    let amphipods = input
        .chars()
        .filter_map(|ch| match ch {
            'A' => Some(Amphipod::A),
            'B' => Some(Amphipod::B),
            'C' => Some(Amphipod::C),
            'D' => Some(Amphipod::D),
            _ => None,
        })
        .collect::<Vec<_>>();

    assert_eq!(amphipods.len(), 8);
    amphipods
}

pub fn parse_initial_state1(input: &str) -> IResult<&str, State<2>> {
    let amphipods = parse_amphipods(input);
    let state = State {
        hallway: [None; 11],
        rooms: [
            [Some(amphipods[0]), Some(amphipods[4])],
            [Some(amphipods[1]), Some(amphipods[5])],
            [Some(amphipods[2]), Some(amphipods[6])],
            [Some(amphipods[3]), Some(amphipods[7])],
        ],
    };

    Ok((input, state))
}

pub fn parse_initial_state2(input: &str) -> IResult<&str, State<4>> {
    let amphipods = parse_amphipods(input);
    let state = State {
        hallway: [None; 11],
        rooms: [
            [amphipods[0], Amphipod::D, Amphipod::D, amphipods[4]].map(Some),
            [amphipods[1], Amphipod::C, Amphipod::B, amphipods[5]].map(Some),
            [amphipods[2], Amphipod::B, Amphipod::A, amphipods[6]].map(Some),
            [amphipods[3], Amphipod::A, Amphipod::C, amphipods[7]].map(Some),
        ],
    };

    Ok((input, state))
}
