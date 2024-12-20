extern crate rust_aoc;

use crate::rust_aoc::day18;
use aoc_util::day_input;

fn main() {
    let input = day_input(2024, 18);
    let p1 = day18::part1(&input);
    let p2 = day18::part2(&input);
    println!("{}", p1);
}
