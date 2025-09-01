use aoc::io::File;
use day_01_not_quite_lisp::part2::solve;

#[tracing::instrument]
fn main() -> anyhow::Result<()> {
    let floors = File::Input(2015, 1).read()?;
    let result = solve(&floors);

    println!("{}", result.unwrap());
    Ok(())
}
