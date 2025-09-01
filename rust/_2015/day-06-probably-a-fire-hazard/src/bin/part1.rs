use anyhow::anyhow;
use aoc::io::File;
use day_06_probably_a_fire_hazard::parse::parse_instructions;
use day_06_probably_a_fire_hazard::part1::solve;

#[tracing::instrument]
fn main() -> anyhow::Result<()> {
    let input = File::Input(2015, 6).read()?;
    let (_, instructions) =
        parse_instructions(&input).map_err(|err| anyhow!("nom error: {err:?}"))?;
    let result = solve(&instructions);

    println!("{}", result);
    Ok(())
}
