extern crate rust_aoc;

use crate::rust_aoc::day8;
use aoc_util::day_input;

fn main() {
    let input = day_input(2024, 8);
    let p1 = day8::part1(&input);
    let p2 = day8::part2(&input);
    println!("{} {}", p1, p2);
}
