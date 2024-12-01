extern crate rust_aoc;
use rust_aoc::day1::{part1, part2};
use aoc_util::day_input;

fn main() {
    let inp = day_input(2024, 1);
    let p1 = part1(&inp);
    let p2 = part2(&inp);
    println!("p1: {}\np2: {}", p1, p2);
}
