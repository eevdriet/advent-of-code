use aoc::io::File;
use day_04_the_ideal_stocking_stuffer::find_leading_zeroes_hash;

#[tracing::instrument]
fn main() -> anyhow::Result<()> {
    let secret = File::Input(2015, 4).read()?;
    let result = find_leading_zeroes_hash(&secret, 5);

    println!("{}", result);
    Ok(())
}
