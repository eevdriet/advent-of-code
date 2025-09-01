use anyhow::anyhow;
use aoc::io::File;
use {{crate_name}}::parse::parse_input;
use {{crate_name}}::part1::solve;

#[tracing::instrument]
fn main() -> anyhow::Result<()> {
    let input = File::Input({{year}}, {{day}}).read()?;
    let (_, data) = parse_input(&input).map_err(|err| anyhow!("nom error: {err:?}"))?;
    let result = solve(&data);

    println!("{}", result);
    Ok(())
}
