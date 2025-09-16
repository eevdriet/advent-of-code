#[repr(u8)]
#[derive(Copy, Clone, Debug, Eq, PartialEq)]
pub enum Amphipod {
    A = 0,
    B = 1,
    C = 2,
    D = 3,
}

impl Amphipod {
    pub fn from_room_index(room_index: usize) -> Self {
        assert!(room_index < 4);
        unsafe { std::mem::transmute(room_index as u8) }
    }

    pub fn energy(&self) -> usize {
        10usize.pow(*self as u32)
    }

    pub fn target_room_index(&self) -> usize {
        *self as usize
    }
}
