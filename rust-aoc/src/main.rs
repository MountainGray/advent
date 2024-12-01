extern crate rust_aoc;

use std::fs::File;
use std::io::{self, Read};

fn read_file(filename: &str) -> io::Result<String> {
    let mut file = File::open(filename)?; // Open the file
    let mut contents = String::new(); // Create a string to store the contents
    file.read_to_string(&mut contents)?; // Read the file's content into the string
    Ok(contents) // Return the content
}

use rust_aoc::day1::{part1, part2};
use std::time::Instant;
use aoc_util::day_input;
fn main() {
    let inp = day_input(2024, 1);
    println!("input len: {}", (&inp).lines().count());
    let p1 = part1(&inp);
    let p2 = part2(&inp);
    println!("p1: {}\n p2: {}", p1, p2);
}
