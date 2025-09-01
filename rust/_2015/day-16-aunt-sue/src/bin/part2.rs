use anyhow::anyhow;
use aoc::io::File;
use day_16_aunt_sue::GIFTS;
use day_16_aunt_sue::parse::parse_tapes;
use day_16_aunt_sue::part2::{ORDERINGS, solve};

#[tracing::instrument]
fn main() -> anyhow::Result<()> {
    let input = File::Input(2015, 16).read()?;
    let (_, tapes) = parse_tapes(&input).map_err(|err| anyhow!("nom error: {err:?}"))?;
    let aunts = solve(&tapes, &GIFTS, &ORDERINGS);

    assert_eq!(aunts.len(), 1);
    println!("{}", aunts.first().unwrap());
    Ok(())
}
