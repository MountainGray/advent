use core::panic;
use std::io;

use regex::Regex;

struct Guard {
    px: i32,
    py: i32,
    vx: i32,
    vy: i32,
}

const DX: i32 = 101;
const DY: i32 = 103;

fn print_grid(guards: &[Guard]) {
    for y in 0..DY {
        for x in 0..DX {
            if guards.iter().any(|g| g.px == x && g.py == y) {
                print!("X");
            } else {
                print!(".");
            }
        }
        println!();
    }
}

#[aoc(day14, part1)]
pub fn part1(input: &str) -> i32 {
    let re = Regex::new(r"-?\d+").unwrap();
    let mut guards: Vec<Guard> = Vec::new();

    for rbt in input.lines() {
        let nums: Vec<i32> = re
            .captures_iter(rbt)
            .filter_map(|v| v.get(0))
            .filter_map(|v| v.as_str().parse().ok())
            .collect();
        let [px, py, vx, vy] = nums[..] else {
            panic!("Invalid line")
        };
        guards.push(Guard { px, py, vx, vy });
    }

    for _ in 0..100 {
        for g in guards.iter_mut() {
            let nx = (g.px + g.vx).rem_euclid(DX);
            let ny = (g.py + g.vy).rem_euclid(DY);
            g.px = nx;
            g.py = ny;
        }
    }
    let (mut q1, mut q2, mut q3, mut q4) = (0, 0, 0, 0);
    for g in guards.iter() {
        if g.px < DX / 2 && g.py < DY / 2 {
            q1 += 1;
        }
        if g.px > DX / 2 && g.py < DY / 2 {
            q2 += 1;
        }
        if g.px < DX / 2 && g.py > DY / 2 {
            q3 += 1;
        }
        if g.px > DX / 2 && g.py > DY / 2 {
            q4 += 1;
        }
    }
    q1 * q2 * q3 * q4
}

// Stupid puzzle, requires visual inspection to find when the tree is printed out
// TODO: maybe fix this at some point... unlikely
pub fn part2(input: &str) {
    let re = Regex::new(r"-?\d+").unwrap();
    let mut guards: Vec<Guard> = Vec::new();

    for rbt in input.lines() {
        let nums: Vec<i32> = re
            .captures_iter(rbt)
            .filter_map(|v| v.get(0))
            .filter_map(|v| v.as_str().parse().ok())
            .collect();
        let [px, py, vx, vy] = nums[..] else {
            panic!("Invalid line")
        };
        guards.push(Guard { px, py, vx, vy });
    }

    for s in 0..10000 {
        for g in guards.iter_mut() {
            let nx = (g.px + g.vx).rem_euclid(DX);
            let ny = (g.py + g.vy).rem_euclid(DY);
            g.px = nx;
            g.py = ny;
        }
        if (s - 27) % 101 == 0 {
            println!("{}", s);
            print_grid(&guards);
            let mut buf = String::new();
            let _ = io::stdin().read_line(&mut buf);
        }
    }
}
