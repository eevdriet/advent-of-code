use anyhow::anyhow;
use aoc::io::File;
use day_23_amphipod::parse::parse_initial_state1;
use day_23_amphipod::part1::solve_part1;

#[tracing::instrument]
fn main() -> anyhow::Result<()> {
    let input = File::Input(2021, 23).read()?;
    let (_, state) = parse_initial_state1(&input).map_err(|err| anyhow!("nom error: {err:?}"))?;
    let result = solve_part1(&state);

    println!("{}", result);
    Ok(())
}
