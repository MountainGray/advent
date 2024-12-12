use memoize::memoize;

#[memoize]
fn get_numrock(rock: u64, rounds: u32) -> u64 {
    if rounds == 0 {
        return 1;
    }

    if rock == 0 {
        get_numrock(1, rounds - 1)
    } else {
        let nd = u64::ilog10(rock) + 1;
        if nd % 2 == 0 {
            let mut ans = 0;
            let f = rock / u64::pow(10, nd / 2);
            let r = rock - f * u64::pow(10, nd / 2);
            ans += get_numrock(f, rounds - 1);
            ans += get_numrock(r, rounds - 1);
            ans
        } else {
            get_numrock(rock * 2024, rounds - 1)
        }
    }
}

#[aoc(day11, part1)]
pub fn part1(input: &str) -> u64 {
    input
        .trim()
        .split(" ")
        .map(|v| v.parse().unwrap())
        .map(|v| get_numrock(v, 25))
        .sum()
}

#[aoc(day11, part2)]
pub fn part2(input: &str) -> u64 {
    input
        .trim()
        .split(" ")
        .map(|v| v.parse().unwrap())
        .map(|v| get_numrock(v, 75))
        .sum()
}
