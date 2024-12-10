extern crate rust_aoc;

extern crate aoc_runner;
extern crate aoc_runner_derive;

//use aoc_runner_derive::aoc_main;
//aoc_main! { lib = rust_aoc }
use aoc_util::day_input;
use rust_aoc::{day1::part1, day8::*};
fn main() {
    let inp = day_input(2024, 8);
    let ans = part1(&inp);
    println!("{}", ans);
}
