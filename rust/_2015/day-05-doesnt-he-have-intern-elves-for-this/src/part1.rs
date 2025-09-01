pub fn solve(words: &[&str]) -> usize {
    words
        .iter()
        .filter(|word| {
            // Verify how many vowels are contained in the word
            let n_vowels = word
                .chars()
                .filter(|letter| matches!(letter, 'a' | 'e' | 'i' | 'o' | 'u'))
                .count();

            // Verify if two consecutive characters are the same, i.e. repeating
            let has_repeat = word
                .chars()
                .zip(word.chars().skip(1))
                .any(|(first, second)| first == second);

            // Verify if the word contains forbidden patterns
            let forbidden = ["ab", "cd", "pq", "xy"]
                .iter()
                .any(|pattern| word.contains(pattern));

            n_vowels >= 3 && has_repeat && !forbidden
        })
        .count()
}
