use md5::Digest;
use std::collections::HashSet;

pub fn parse(input: &str) -> String {
    input.trim().to_string()
}

pub fn part_one(input: &str) -> u32 {
    for i in 0.. {
        let digest = md5::compute(format!("{}{}", input, i));
        if digest[0] == 0 && digest[1] == 0 && digest[2] < 16 {
            return i;
        }
    }
    unreachable!()
}

pub fn part_two(input: &str) -> u32 {
    for i in 0.. {
        let digest = md5::compute(format!("{}{}", input, i));
        if digest[0] == 0 && digest[1] == 0 && digest[2] == 0 {
            return i;
        }
    }
    unreachable!()
}
