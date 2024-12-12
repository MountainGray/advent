const WALL: u8 = b'#';
const G: u8 = b'^';
const N: usize = 130;

// TODO: Change accept from enter to tab jacob...
use std::collections::HashSet;

#[aoc(day6, part1)]
pub fn part1(input: &str) -> usize {
    let inp = input.as_bytes();
    let (mut x, mut y) = (0, 0);
    let (mut dx, mut dy) = (0, -1);

    for idy in 0..N {
        for idx in 0..N {
            if inp[idy * (N + 1) + idx] == G {
                (x, y) = (idx as i32, idy as i32);
            }
        }
    }

    let mut visited: HashSet<(i32, i32)> = HashSet::new();
    loop {
        visited.insert((x, y));
        let (nx, ny) = (x + dx, y + dy);
        if nx < 0 || nx as usize >= N || ny < 0 || ny as usize >= N {
            break;
        }
        let c = inp[(ny as usize) * (N + 1) + nx as usize];
        if c != WALL {
            (x, y) = (nx, ny);
        } else {
            (dx, dy) = (-dy, dx);
        };
    }
    visited.len()
}

pub fn try_loop(pos: (i32, i32), dir: (i32, i32), grid: &[u8], twall: (i32, i32)) -> bool {
    let mut looped: HashSet<((i32, i32), (i32, i32))> = HashSet::new();
    let (mut dx, mut dy) = dir;
    let (mut x, mut y) = pos;
    loop {
        if looped.contains(&((x, y), (dx, dy))) {
            return true;
        } else {
            looped.insert(((x, y), (dx, dy)));
        }
        let (nx, ny) = (x + dx, y + dy);
        if nx < 0 || nx as usize >= N || ny < 0 || ny as usize >= N {
            return false;
        }
        if grid[(ny as usize) * (N + 1) + nx as usize] != WALL && (nx, ny) != twall {
            (x, y) = (nx, ny);
        } else {
            (dx, dy) = (-dy, dx);
        }
    }
}

#[aoc(day6, part2)]
pub fn part2(input: &str) -> usize {
    let inp = input.as_bytes();
    let (mut x, mut y) = (0, 0);
    let (mut dx, mut dy) = (0, -1);

    for idy in 0..N {
        for idx in 0..N {
            if inp[idy * (N + 1) + idx] == G {
                (x, y) = (idx as i32, idy as i32);
            }
        }
    }
    let mut answer = 0;

    let mut visited: HashSet<(i32, i32)> = HashSet::new();
    loop {
        visited.insert((x, y));
        let (nx, ny) = (x + dx, y + dy);
        if nx < 0 || nx as usize >= N || ny < 0 || ny as usize >= N {
            break;
        }
        if inp[(ny as usize) * (N + 1) + nx as usize] != WALL {
            // can't block path we have already traveled
            if !visited.contains(&(nx, ny)) {
                let is_loop = try_loop((x, y), (dx, dy), inp, (nx, ny));
                if is_loop {
                    answer += 1;
                }
            }
            (x, y) = (nx, ny);
        } else {
            (dx, dy) = (-dy, dx);
        };
    }
    answer
}
