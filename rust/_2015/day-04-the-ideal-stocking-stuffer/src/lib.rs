use md5::{Digest, Md5};

fn starts_with_n_zeros(bytes: &[u8], n_zeros: usize) -> bool {
    let n_full_bytes = n_zeros / 2;
    let need_half_nibble = n_zeros % 2 == 1;

    // All required full bytes must be zero
    if bytes[..n_full_bytes].iter().any(|&bit| bit != 0) {
        return false;
    }

    // If we need a half byte, check the high nibble of the next byte
    if need_half_nibble && bytes[n_full_bytes] >> 4 != 0 {
        return false;
    }

    true
}

pub fn find_leading_zeroes_hash(secret: &str, n_zeros: usize) -> usize {
    (1..)
        .find(|&num| {
            let mut hasher = Md5::new();
            hasher.update(secret.as_bytes());
            hasher.update(num.to_string().as_bytes());

            let digest = hasher.finalize();
            starts_with_n_zeros(&digest, n_zeros)
        })
        .unwrap()
}
