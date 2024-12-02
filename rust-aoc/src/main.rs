extern crate rust_aoc;
use aoc_util::day_input;
use rust_aoc::day2::{part1, part2};

fn main() {
    let inp = day_input(2024, 2);
    let p1 = part1(&inp);
    let p2 = part2(&inp);
    println!("p1: {}\np2: {}", p1, p2);
}
