pub fn parse(input: &str) -> Vec<i32> {
    input
        .chars()
        .map(|c| match c {
            '(' => 1,
            ')' => -1,
            _ => 0,
        })
        .collect()
}

pub fn part_one(input: &[i32]) -> i32 {
    input.iter().sum()
}

pub fn part_two(input: &[i32]) -> usize {
    let mut floor = 0;
    for (idx, i) in input.iter().enumerate() {
        floor += i;
        if floor == -1 {
            return idx + 1;
        }
    }
    unreachable!();
}
