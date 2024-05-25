use aoc::day_input;

pub fn part_one(input: &str) -> u64{
    input.lines()
    .map(|x| x.parse::<u64>().unwrap())
    .map(|x| x/3 - 2).sum()
}

pub fn part_two(input: &str) -> u64 {
    input.lines()
    .map(|x| x.parse::<u64>().unwrap())
    .map(|x| x/3 - 2).sum()
}


#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn input_p1() {
        let input = day_input(2019, 1);
        let result = part_one(input.as_str());
        println!("{}", result)
    }
}