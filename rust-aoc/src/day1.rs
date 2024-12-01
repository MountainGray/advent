use std::iter::zip;
use std::num;
use itertools::Itertools;
//#[aoc(day1, part1, Chars)]
pub fn part1(input: &str) -> i32 {
    let mut va = Vec::new();
    let mut vb = Vec::new();

    for l in input.lines() { 
        va.push(l[0..5].parse::<i32>().unwrap());
        vb.push(l[8..].parse::<i32>().unwrap());
    }
    va.sort();
    vb.sort();
    zip(va.iter(), vb.iter()).map(|(a, b)| (a-b).abs()).sum()
}

pub fn part2(input: &str) -> i32 {
    let s = input.lines().count();
    let mut va = Vec::with_capacity(s);
    let mut vb = Vec::with_capacity(s);

    for l in input.lines() { 
        va.push(l[0..5].parse::<i32>().unwrap());
        vb.push(l[8..].parse::<i32>().unwrap());
    }

    let c  = vb.iter().counts();
    va.iter()
      .map(|x| {
        match c.get(x) {
                Some(c) => x * (*c as i32),
                None => 0
        }})
      .sum()
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};
}
