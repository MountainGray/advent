const N: usize = 140 + 1;

#[aoc(day4, part1)]
pub fn part1(input: &str) -> u32 {
    let inp = input.as_bytes();
    let mut ans = 0;
    for i in 0..(N - 1) {
        for j in 0..(N - 1) {
            let idx = i * N + j;
            if j < N - 4 {
                let h = &inp[idx..idx + 4];
                if h == "XMAS".as_bytes() || h == "SAMX".as_bytes() {
                    ans += 1;
                }
            }
            // vertical constraint
            if i < N - 4 {
                let v = [inp[idx], inp[idx + N], inp[idx + N * 2], inp[idx + N * 3]];
                if v == "XMAS".as_bytes() || v == "SAMX".as_bytes() {
                    ans += 1;
                }
                if j < N - 4 {
                    let d = [
                        inp[idx],
                        inp[idx + N + 1],
                        inp[idx + N * 2 + 2],
                        inp[idx + N * 3 + 3],
                    ];
                    if d == "XMAS".as_bytes() || d == "SAMX".as_bytes() {
                        ans += 1;
                    }

                    let d = [
                        inp[idx + 3],
                        inp[idx + N + 2],
                        inp[idx + N * 2 + 1],
                        inp[idx + N * 3],
                    ];
                    if d == "XMAS".as_bytes() || d == "SAMX".as_bytes() {
                        ans += 1;
                    }
                }
            }
        }
    }
    ans
}

#[aoc(day4, part2)]
pub fn part2(input: &str) -> u32 {
    let inp = input.as_bytes();
    let mut ans = 0;
    for i in 0..(N - 1) {
        for j in 0..(N - 1) {
            let idx = i * N + j;
            if i < N - 3 {
                if j < N - 3 {
                    let d = [inp[idx], inp[idx + N + 1], inp[idx + N * 2 + 2]];
                    if !(d == "MAS".as_bytes() || d == "SAM".as_bytes()) {
                        continue;
                    }
                    let d2 = [inp[idx + 2], inp[idx + N + 1], inp[idx + N * 2]];
                    if d2 == "MAS".as_bytes() || d2 == "SAM".as_bytes() {
                        ans += 1;
                    }
                }
            }
        }
    }
    ans
}
