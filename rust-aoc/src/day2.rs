use itertools::all;

pub fn part1(input: &str) -> u32 {
    let numvs = input.lines().map(|l| {
        l.split(" ")
            .filter_map(|v| v.parse::<u32>().ok())
            .collect::<Vec<u32>>()
    });
    let mut ans = 0;

    'outer: for v in numvs {
        let mut asc = true;
        let mut dec = true;

        for (x, y) in v.iter().zip(v.iter().skip(1)) {
            // note: what if signed is faster for this?
            if asc && x >= y {
                if !dec {
                    continue 'outer;
                }
                asc = false;
            }
            if dec && x <= y {
                if !asc {
                    continue 'outer;
                }
                dec = false;
            }
            if x.abs_diff(*y) > 3 {
                continue 'outer;
            }
        }
        ans += 1;
    }
    ans
}

pub fn part2(input: &str) -> u32 {
    let numvs = input.lines().map(|l| {
        l.split(" ")
            .filter_map(|v| v.parse::<u32>().ok())
            .collect::<Vec<u32>>()
    });
    let mut ans = 0;
    for v in numvs {
        for i in 0..v.len() {
            let mut nv = v.clone();
            nv.remove(i);
            let pairs = nv.iter().zip(nv.iter().skip(1));
            if all(pairs.clone(), |(x, y)| x.abs_diff(*y) <= 3)
                && (all(pairs.clone(), |(x, y)| x < y) || all(pairs, |(x, y)| x > y))
            {
                ans += 1;
                break;
            }
        }
    }
    ans
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};
}
