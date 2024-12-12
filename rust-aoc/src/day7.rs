#[aoc(day7, part1)]
pub fn part1(input: &str) -> i64 {
    let inp: Vec<(i64, Vec<i64>)> = input
        .trim()
        .lines()
        .map(|l| {
            let v: Vec<i64> = l
                .replace(":", "")
                .split_whitespace()
                .map(|x| x.parse().unwrap())
                .collect();
            (v[0], v.into_iter().skip(1).collect())
        })
        .collect();
    let mut ans = 0;
    for (s, vs) in inp {
        let mut ts = vec![vs[0]];
        for rv in vs[1..].iter() {
            let mut nv = Vec::new();
            for i in ts {
                nv.push(rv * i);
                nv.push(rv + i);
            }
            ts = nv;
        }
        if ts.contains(&s) {
            ans += s;
        }
    }
    ans
}

// TODO make translation on raw bytes including newlines...
#[aoc(day7, part2)]
pub fn part2(input: &str) -> i64 {
    let inp: Vec<(i64, Vec<i64>)> = input
        .trim()
        .lines()
        .map(|l| {
            let v: Vec<i64> = l
                .replace(":", "")
                .split_whitespace()
                .map(|x| x.parse().unwrap())
                .collect();
            (v[0], v.into_iter().skip(1).collect())
        })
        .collect();
    let mut ans = 0;
    for (s, vs) in inp {
        let mut ts = vec![vs[0]];
        for rv in vs[1..].iter() {
            let mut nv = Vec::new();
            for i in ts {
                nv.push(rv * i);
                nv.push(rv + i);
                let rs = i64::ilog10(*rv) + 1;
                nv.push(i * i64::pow(10, rs) + rv);
            }
            ts = nv;
        }
        if ts.contains(&s) {
            ans += s;
        }
    }
    ans
}
