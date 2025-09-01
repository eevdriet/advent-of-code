use std::collections::HashMap;
use aoc::io::{read, File};

#[derive(Debug, PartialEq, Eq)]
struct Hand {
    cards: Vec<u8>,
    bid: usize,
    jokers: bool,
}

impl PartialOrd for Hand {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Hand {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        match self.score().cmp(&other.score()) {
            std::cmp::Ordering::Equal => self.cards.cmp(&other.cards),
            other => other
        }
    }
}

impl Hand {
    fn new(cards: Vec<u8>, bid: usize, jokers: bool) -> Self {
        Self { cards, bid, jokers }
    }

    fn char_value(ch: char, jokers: bool) -> u8 {
        match ch {
            'J' => match jokers {
                true => 1,
                false => 11
            },
            'T' => 10,
            'Q' => 12,
            'K' => 13,
            'A' => 14,
            _ => ch as u8 - b'0'
        }
    }

    fn parse(input: &str, jokers: bool) -> Self {
        let parts = input.split_whitespace().collect::<Vec<_>>();

        let cards = parts[0].chars().map(|ch| Hand::char_value(ch, jokers)).collect::<Vec<_>>();
        let bid = parts[1].parse::<usize>().unwrap();

        Hand::new(cards, bid, jokers)
    }

    fn score(&self) -> u8 {
        let mut counts: HashMap<u8, usize> = HashMap::new();
        let mut max_card = 0;
        let mut max_count = 0;

        if !self.jokers {
            // Count all cards
            self.cards.iter().for_each(|card| *counts.entry(*card).or_insert(0) += 1 );
        }
        else {
            // Count all non-joker cards
            self.cards.iter().filter(|card| **card != 1).for_each(|card| *counts.entry(*card).or_insert(0) += 1);

            // Determine which card appears most often
            for (card, count) in counts.iter() {
                if *count > max_count {
                    max_card = *card;
                    max_count = *count;
                }
            }

            // Use all jokers as the most often appearing card
            let n_jokers = self.cards.iter().filter(|card| **card == 1).count();
            *counts.entry(max_card).or_insert(0) += n_jokers;
        }

        // Determine the score based on the multiplicity of the cards
        max_count = *counts.values().max().unwrap();

        match counts.len() {
            1 => 7,                 // five-of-a-kind
            2 => match max_count {
                4 => 6,             // four-of-a-kind
                _ => 5,             // full-house
            },
            3 => match max_count {
                3 => 4,             // three-of-a-kind
                _ => 3,             // two-pair
            },
            4 => 2,                 // pair
            _ => 1                  // high-card
        }
    }
}

fn part1(txt: &str) -> usize {
    let mut hands = txt.lines().map(|line| Hand::parse(line, false)).collect::<Vec<_>>();
    hands.sort();

    hands.iter().enumerate().map(|(iter, hand)| (iter + 1) * hand.bid).sum::<usize>()
}

fn part2(txt: &str) -> usize {
    let mut hands = txt.lines().map(|line| Hand::parse(line, true)).collect::<Vec<_>>();
    hands.sort();

    hands.iter().enumerate().map(|(iter, hand)| (iter + 1) * hand.bid).sum::<usize>()
}

fn main() {
    let txt = read(&File::Input(7)).unwrap();

    println!("Part 1: {}", part1(&txt));
    println!("Part 2: {}", part2(&txt));
}
