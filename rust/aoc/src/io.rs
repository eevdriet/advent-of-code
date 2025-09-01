use std::fs::read_to_string;
use std::path::PathBuf;
use std::str::FromStr;

pub enum File {
    Input(u32, u32),
    Example(u32, u32),
    Custom(u32, u32, String),
}

impl File {
    pub fn path(&self) -> PathBuf {
        // Get the path to the data
        let mut base = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
        base.pop();
        base.pop();
        base.push("data");

        // Determine the specific file within the data
        base.push(match &self {
            File::Input(year, day) => format!("{year}/{day}.input"),
            File::Example(year, day) => format!("{year}/{day}.example"),
            File::Custom(year, day, format) => format!("{year}/{day}.{format}"),
        });

        base
    }

    pub fn read(&self) -> std::io::Result<String> {
        read_to_string(self.path())
    }
}

/// Read the file in one by one
///
/// * `file`: File to read in
pub fn read_one_per_line<T>(file: &File) -> std::io::Result<Vec<T>>
where
    T: FromStr,
{
    let txt = read_to_string(file.path())?;

    // Split the whole input file on new lines and parse each individually
    Ok(txt
        .lines()
        .filter_map(|line| line.parse::<T>().ok())
        .collect())
}

/// Read the file in line by line, converting each to a vector
///
/// * `file`: File to read in
/// * `func`: Function that maps from the characters of the file
pub fn read_vec_per_line<T, F>(file: &File, func: F) -> std::io::Result<Vec<Vec<T>>>
where
    T: FromStr,
    F: Fn(char) -> Option<T>,
{
    let txt = read_to_string(file.path())?;

    Ok(txt
        .lines()
        .map(|line| line.chars().map(|c| func(c).unwrap()).collect())
        .collect())
}
