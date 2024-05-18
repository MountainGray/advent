use aoc_util::day_input;
use serde::{Deserialize, Serialize};
use serde_json::Result;
use std::env;

#[derive(Serialize, Deserialize)]
struct ProblemInput {
    year: i32,
    day: i32,
    input: String,
}

fn main() {
    use advent::year_2015::day04::*;
    let input = day_input(2015, 4);
    let input = parse(&input);
    let part1 = part_one(&input).to_string();
    let part2 = part_two(&input).to_string();

    println!("Part 1: {}\nPart 2: {}", part1, part2);
}
