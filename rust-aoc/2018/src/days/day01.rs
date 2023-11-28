use aoc::{day_input, AOCResult};


fn part_one() -> AOCResult {
    let input = day_input(2018, 1);
    let sum = input.lines().map(|str| str.parse::<i64>().unwrap()).sum();

    AOCResult::Number(sum)
}

fn part_two() -> AOCResult {
    let input = day_input(2018, 1);

    let mut sum = 0;
    let mut seen = Vec::new();

    let vals : Vec<i64> = input.lines().map(|str| str.parse::<i64>().unwrap()).collect();


    //println!("{:?}", vals);

    loop {
        for val in vals[..10].iter() {
            sum += val;
            if sum == 77674 {
                print!("fuck");
            }
            //println!("sum: {}", sum);
            if seen.contains(&sum) {
                return AOCResult::Number(sum);
            } else {
                seen.push(sum.clone());
                //println!("{:?}", seen);
            }
        }

    }

    AOCResult::Number(0)
}

#[cfg(test)]
mod tests {
    use super::{part_one, part_two};
    use aoc::day_input;

    #[test]
    fn display_input() {
        let input = day_input(2018, 1);
        println!("{}", input);
    }

    #[test]
    fn p1() {
        let result = part_one();
        println!("{}", result)
    }

    #[test]
    fn p2() {
        let result = part_two();
        println!("{}", result)
    }
}
