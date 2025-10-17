use anyhow::anyhow;
use aoc::io::File;
use day_10_hoof_it::parse::parse_grid;
use day_10_hoof_it::part1::solve;

#[tracing::instrument]
fn main() -> anyhow::Result<()> {
    let input = File::Input(2024, 10).read()?;
    let (_, data) = parse_grid(&input).map_err(|err| anyhow!("nom error: {err:?}"))?;
    let result = solve(&data);

    println!("{}", result);
    Ok(())
}
