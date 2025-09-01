pub fn solve(floors: &str) -> isize {
    floors.chars().fold(0, |floor, step| {
        floor
            + match step {
                ')' => -1,
                '(' => 1,
                _ => 0,
            }
    })
}
