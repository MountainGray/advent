extern crate rust_aoc;

use crate::rust_aoc::day14;
use aoc_util::day_input;

fn main() {
    let input = day_input(2024, 14);
    let p1 = day14::part1(&input);
    //let p2 = day12::part2(&input);
    println!("{}", p1);
}
