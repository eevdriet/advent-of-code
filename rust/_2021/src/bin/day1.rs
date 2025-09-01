use aoc::io::{read_one_per_line, File};

fn descending_window(txt: &Vec<u32>, size: usize) -> usize {
    txt.windows(size)
        .filter(|win| win[0] < win[size - 1])
        .collect::<Vec<_>>()
        .len()
}

fn main() {
    let calories = read_one_per_line::<u32>(&File::Input(1)).unwrap();

    println!("Part 1: {}", descending_window(&calories, 2));
    println!("Part 2: {}", descending_window(&calories, 4));
}
