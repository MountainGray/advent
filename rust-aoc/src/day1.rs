use rdxsort::*;
use std::iter::zip;

#[aoc(day1, part1)]
pub fn part1(input: &str) -> u32 {
    let mut va = [0; 1000];
    let mut vb = [0; 1000];

    for i in 0..1000 {
        va[i] = input[(i * 14)..(i * 14 + 5)].parse::<u32>().unwrap();
        vb[i] = input[(i * 14 + 8)..(i * 14 + 13)].parse::<u32>().unwrap();
    }

    va.rdxsort();
    vb.rdxsort();

    zip(va.iter(), vb.iter())
        .map(|(a, b)| (a.abs_diff(*b)))
        .sum()
}

#[aoc(day1, part2)]
pub fn part2(input: &str) -> u32 {
    let mut va = [0; 1000];
    let mut vb = [0; 1000];

    for i in 0..1000 {
        va[i] = input[(i * 14)..(i * 14 + 5)].parse::<u32>().unwrap();
        vb[i] = input[(i * 14 + 8)..(i * 14 + 13)].parse::<u32>().unwrap();
    }

    let mut ftable = [0; 100000];

    for x in vb {
        ftable[x as usize] += 1;
    }

    va.iter().fold(0, |acc, x| acc + x * ftable[*x as usize])
}

pub fn parse(input: &str) {
    let mut va = [0; 1000];
    let mut vb = [0; 1000];

    for i in 0..1000 {
        va[i] = input[(i * 14)..(i * 14 + 5)].parse::<u32>().unwrap();
        vb[i] = input[(i * 14 + 8)..(i * 14 + 13)].parse::<u32>().unwrap();
    }
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};
}
