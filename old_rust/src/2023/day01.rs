use aoc::day_input;

fn part_one(input: &str) -> Option<u32>{
    let mut line_digits = Vec::<Vec<u32>>::new();

    for line in input.lines() {
        line_digits.push(
            line.chars()
                .filter_map(
                    |x| x.to_digit(10)
                )
                .collect()
        );
    }

    let ans = line_digits.iter()
        .map(|digits| digits.first().unwrap() * 10 + digits.last().unwrap())
        .sum();

    Some(ans)
}

fn part_two(input: &str) -> Option<u32> {
    let mut line_digits = Vec::<Vec<(usize, u32)>>::new();

    let digit_map = vec![
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9)
    ];


    for line in input.lines() {
        let mut digits : Vec<(usize, u32)> = line.chars()
            .enumerate()
            .map(|(idx, chr)| (idx, chr.to_digit(10)))
            .filter(|(_,chr)| chr.is_some())
            .map(|(idx, chr)| (idx, chr.unwrap()))
            .collect();

        for (num, val) in digit_map.iter() {
            for (idx, _ ) in line.match_indices(num) {
                digits.push((idx, *val))
            }
        }
        digits.sort();
        line_digits.push(digits)
    }

    let ans = line_digits.iter().map(|line|
        line[0].1 * 10 + line[line.len()-1].1
    ).sum();

    Some(ans)
}


#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn sample_p1() {
        let input = "1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet";
        let result = part_one(input);
        assert_eq!(result, Some(142))
    }

    #[test]
    fn run_p1() {
        let input = day_input(2023, 1);
        let result = part_one(input.as_str());
        match result {
            Some(ans) => println!("{}", ans),
            None => println!("failed to get answer")
        }
    }

    #[test]
    fn sample_p2() {
        let input = "two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen";
        let result = part_two(input);
        assert_eq!(result, Some(281))
    }

    #[test]
    fn run_p2() {
        let input = day_input(2023, 1);
        let result = part_two(input.as_str());
        match result {
            Some(ans) => println!("{}", ans),
            _ => println!("failed to get answer")
        }
    }
}
