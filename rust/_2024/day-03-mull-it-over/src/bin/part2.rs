use anyhow::anyhow;
use aoc::io::File;
use day_03_mull_it_over::parse::parse_instructions;
use day_03_mull_it_over::part2::solve;

#[tracing::instrument]
fn main() -> anyhow::Result<()> {
    let input = File::Input(2024, 3).read()?;
    let (_, data) = parse_instructions(&input).map_err(|err| anyhow!("nom error: {err:?}"))?;
    let result = solve(&data);

    println!("{}", result);
    Ok(())
}
