use anyhow::anyhow;
use aoc::io::File;
use day_02_i_was_told_there_would_be_no_math::parse::parse_gifts;
use day_02_i_was_told_there_would_be_no_math::part2::solve;

#[tracing::instrument]
fn main() -> anyhow::Result<()> {
    let input = File::Input(2015, 2).read()?;
    let (_, data) = parse_gifts(&input).map_err(|err| anyhow!("nom error: {err:?}"))?;
    let result = solve(&data);

    println!("{}", result);
    Ok(())
}
