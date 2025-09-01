pub mod parse;
pub mod part1;
pub mod part2;

pub struct Gift {
    length: usize,
    width: usize,
    height: usize,
}

impl Gift {
    fn dimensions(&self) -> Vec<usize> {
        vec![self.length, self.width, self.height]
    }

    fn smallest_two(&self) -> (usize, usize) {
        let (mut min1, mut min2) = (usize::MAX, usize::MAX);

        for dimension in self.dimensions() {
            if dimension < min1 {
                min2 = min1;
                min1 = dimension;
            } else if dimension < min2 {
                min2 = dimension;
            }
        }

        (min1, min2)
    }

    pub fn wrapping_required(&self) -> usize {
        let surface = 2 * self.length * self.width
            + 2 * self.width * self.height
            + 2 * self.height * self.length;

        let (min1, min2) = self.smallest_two();
        let smallest_side = min1 * min2;

        surface + smallest_side
    }

    pub fn ribbon_required(&self) -> usize {
        // Determine ribbon required for the wrapping paper
        let (min1, min2) = self.smallest_two();
        let wrapping = (2 * min1) + (2 * min2);

        // Do the same for the bow
        let bow = self.dimensions().iter().product::<usize>();

        wrapping + bow
    }
}
