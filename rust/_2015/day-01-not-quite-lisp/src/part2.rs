pub fn solve(floors: &str) -> Option<usize> {
    floors
        .chars()
        .map(|floor| if floor == '(' { 1 } else { -1 })
        .scan(0, |floor, step| {
            *floor += step;
            Some(*floor)
        })
        .position(|floor| floor < 0)
        .map(|floor| floor + 1)
}
