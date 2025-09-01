use anyhow::anyhow;
use aoc::io::File;
use day_17_no_such_thing_as_too_much::parse::parse_containers;
use day_17_no_such_thing_as_too_much::part2::solve;

#[tracing::instrument]
fn main() -> anyhow::Result<()> {
    let input = File::Input(2015, 17).read()?;
    let (_, containers) = parse_containers(&input).map_err(|err| anyhow!("nom error: {err:?}"))?;
    let result = solve(&containers, 150);

    println!("{}", result);
    Ok(())
}
