use std::collections::HashSet;

#[derive(Eq, Hash, PartialEq, Clone)]
struct Santa {
    x: i32,
    y: i32,
}

pub fn parse(input: &str) -> Vec<(i32, i32)> {
    input
        .chars()
        .map(|c| match c {
            '^' => (0, 1),
            'v' => (0, -1),
            '>' => (1, 0),
            '<' => (-1, 0),
            _ => (0, 0),
        })
        .collect()
}

pub fn part_one(input: &[(i32, i32)]) -> i32 {
    let mut santa = Santa { x: 0, y: 0 };

    let mut visited = HashSet::new();
    visited.insert(santa.clone());

    for i in input.iter() {
        santa.x += i.0;
        santa.y += i.1;
        visited.insert(santa.clone());
    }
    visited.len() as i32
}

pub fn part_two(input: &[(i32, i32)]) -> i32 {
    let mut santa = Santa { x: 0, y: 0 };
    let mut robosanta = Santa { x: 0, y: 0 };

    let mut visited = HashSet::new();
    visited.insert(santa.clone());

    for (idx, i) in input.iter().enumerate() {
        if idx % 2 == 0 {
            santa.x += i.0;
            santa.y += i.1;
            visited.insert(santa.clone());
        } else {
            robosanta.x += i.0;
            robosanta.y += i.1;
            visited.insert(robosanta.clone());
        }
    }
    visited.len() as i32
}
