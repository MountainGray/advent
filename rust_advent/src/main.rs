use aoc_util::day_input;
use serde::{Deserialize, Serialize};
use serde_json::Result;
use std::{env, fs};
use advent::*;

#[derive(Serialize, Deserialize)]
pub struct ProblemInput {
    year: i32,
    day: i32,
    input: String,
}

pub struct ProblemSolution {
    part1: String,
    part2: String,

}

// TODO: Testing Macro?

fn main() {
    use advent::year_2019::day01::*;
    let input = day_input(2019, 1);
    let input = parse(&input);
    let part1 = part_one(&input).to_string();
    let part2 = part_two(&input).to_string();

    println!("Part 1: {}\nPart 2: {}", part1, part2);
}

extern crate proc_macro;
use proc_macro::TokenStream;


fn solve(query: ProblemInput) -> String {
    match query {
        ProblemInput {year: 2019, day: 3, input} => {
            let parsed = advent::year_2019::day03::parse(&input);

        },


    } 



}