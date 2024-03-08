use aoc_util::day_input;
use std::env;

fn main() {
    let _args: Vec<String> = env::args().collect();

    use advent::year_2015::day02::*;
    let input = day_input(2015, 2);
    let input = parse(&input);
    let part1 = part_one(&input).to_string();
    let part2 = part_two(&input).to_string();

    println!("Part 1: {}\nPart 2: {}", part1, part2);
}
