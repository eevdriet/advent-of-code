use aoc::io::File;
use day_05_doesnt_he_have_intern_elves_for_this::part1::solve;

#[tracing::instrument]
fn main() -> anyhow::Result<()> {
    let input = File::Input(2015, 5).read()?;
    let words = input.split_whitespace().collect::<Vec<_>>();
    let result = solve(&words);

    println!("{}", result);
    Ok(())
}
