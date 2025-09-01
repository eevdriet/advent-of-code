use anyhow::anyhow;
use aoc::io::File;
use day_03_perfectly_spherical_houses_in_a_vacuum::parse::parse_directions;
use day_03_perfectly_spherical_houses_in_a_vacuum::part1::solve;

#[tracing::instrument]
fn main() -> anyhow::Result<()> {
    let input = File::Input(2015, 3).read()?;
    let (_, directions) = parse_directions(&input).map_err(|err| anyhow!("nom error: {err:?}"))?;
    let result = solve(&directions);

    println!("{}", result);
    Ok(())
}
