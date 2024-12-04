//"((mul\(\d+,\d+\))|(do\(\))|(don't\(\)))"

use regex::Regex;

#[aoc(day3, part1)]
pub fn part1(input: &str) -> u32 {
    let re = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();
    let mut ans = 0;
    for (_, [x, y]) in re.captures_iter(input).map(|c| c.extract()) {
        ans += x.parse::<u32>().unwrap() * y.parse::<u32>().unwrap();
    }
    ans
}
