use anyhow::anyhow;
use aoc::io::File;
use day_02_cube_conundrum::parse::parse_games;
use day_02_cube_conundrum::part1;

#[tracing::instrument]
fn main() -> anyhow::Result<()> {
    // Parse input
    let input = File::Input(2023, 2).read()?;
    let (_, games) = parse_games(&input).map_err(|err| anyhow!("nom error: {err:?}"))?;

    // Find result
    let result = part1::solve(&games);
    println!("{}", result);

    Ok(())
}
