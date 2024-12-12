// TODO make translation on raw bytes including newlines...
use std::collections::{HashMap, HashSet};

#[aoc(day8, part1)]
pub fn part1(input: &str) -> usize {
    // store all tower groups
    let mut ptowers: HashMap<char, Vec<(i32, i32)>> = HashMap::new();

    // gah
    let mdim = input.lines().next().unwrap().len() as i32;

    for (idy, l) in input.lines().enumerate() {
        for (idx, c) in l.chars().enumerate() {
            if c != '.' {
                ptowers.entry(c).or_default().push((idx as i32, idy as i32));
            }
        }
    }

    let mut pos: HashSet<(i32, i32)> = HashSet::new();
    for (_, v) in ptowers {
        for i in 0..v.len() - 1 {
            for j in i + 1..v.len() {
                let (x1, y1) = v[i];
                let (x2, y2) = v[j];
                let ax = x1 + (x1 - x2);
                let ay = y1 + (y1 - y2);
                if 0 <= ax && ax < mdim && 0 <= ay && ay < mdim {
                    pos.insert((ax, ay));
                }
                let ax = x2 + (x2 - x1);
                let ay = y2 + (y2 - y1);
                if 0 <= ax && ax < mdim && 0 <= ay && ay < mdim {
                    pos.insert((ax, ay));
                }
            }
        }
    }
    pos.len()
}

// TODO make translation on raw bytes including newlines...
#[aoc(day8, part2)]
pub fn part2(input: &str) -> usize {
    // store all tower groups
    let mut ptowers: HashMap<char, Vec<(i32, i32)>> = HashMap::new();

    // gah
    let mdim = input.lines().next().unwrap().len() as i32;

    for (idy, l) in input.lines().enumerate() {
        for (idx, c) in l.chars().enumerate() {
            if c != '.' {
                ptowers.entry(c).or_default().push((idx as i32, idy as i32));
            }
        }
    }

    let mut pos: HashSet<(i32, i32)> = HashSet::new();
    for (_, v) in ptowers {
        for i in 0..v.len() - 1 {
            for j in i + 1..v.len() {
                let (x1, y1) = v[i];
                let (x2, y2) = v[j];
                let mut ax = x1;
                let mut ay = y1;
                let dx = x1 - x2;
                let dy = y1 - y2;
                while 0 <= ax && ax < mdim && 0 <= ay && ay < mdim {
                    pos.insert((ax, ay));
                    ax += dx;
                    ay += dy
                }
                let mut ax = x2;
                let mut ay = y2;
                let dx = x2 - x1;
                let dy = y2 - y1;
                while 0 <= ax && ax < mdim && 0 <= ay && ay < mdim {
                    pos.insert((ax, ay));
                    ax += dx;
                    ay += dy
                }
            }
        }
    }
    pos.len()
}
