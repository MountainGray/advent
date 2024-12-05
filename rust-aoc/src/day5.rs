#[aoc(day5, part1)]
pub fn part1(input: &str) -> u32 {
    let (rules, updates) = input.split_once("\n\n").unwrap();

    let rules: Vec<(u32, u32)> = rules
        .split("\n")
        .map(|s| {
            let (x, y) = s.split_once("|").unwrap();
            (x.parse::<u32>().unwrap(), y.parse::<u32>().unwrap())
        })
        .collect();

    let updates: Vec<Vec<u32>> = updates
        .split("\n")
        .map(|l| l.split(",").map(|v| v.parse::<u32>().unwrap()).collect())
        .collect();

    let mut ans = 0;
    for u in updates {
        let mut valid = true;
        for (x, y) in &rules {
            if let (Some(xp), Some(yp)) =
                (u.iter().position(|v| v == x), u.iter().position(|v| v == y))
            {
                if xp > yp {
                    valid = false;
                }
            }
        }
        if valid {
            ans += u[u.len() / 2];
        }
    }
    ans
}

#[aoc(day5, part2)]
pub fn part2(input: &str) -> u32 {
    let (rules, updates) = input.split_once("\n\n").unwrap();

    let rules: Vec<(u32, u32)> = rules
        .split("\n")
        .map(|s| {
            let (x, y) = s.split_once("|").unwrap();
            (x.parse::<u32>().unwrap(), y.parse::<u32>().unwrap())
        })
        .collect();

    let updates: Vec<Vec<u32>> = updates
        .split("\n")
        .map(|l| l.split(",").map(|v| v.parse::<u32>().unwrap()).collect())
        .collect();

    let mut ans = 0;
    for mut u in updates {
        let mut valid = true;
        for (x, y) in &rules {
            if let (Some(xp), Some(yp)) =
                (u.iter().position(|v| v == x), u.iter().position(|v| v == y))
            {
                if xp > yp {
                    valid = false;
                }
            }
        }
        if !valid {
            loop {
                let mut changed = false;
                for (x, y) in &rules {
                    if let (Some(xp), Some(yp)) =
                        (u.iter().position(|v| v == x), u.iter().position(|v| v == y))
                    {
                        if xp > yp {
                            changed = true;
                            u[xp] = *y;
                            u[yp] = *x;
                        }
                    }
                }
                if !changed {
                    break;
                }
            }
            ans += u[u.len() / 2];
        }
    }
    ans
}
