pub fn parse(input: &str) -> Vec<(u32, u32, u32)> {
    input
        .lines()
        .map(|l| {
            let mut vc: Vec<u32> = l.split('x').filter_map(|c| c.parse().ok()).collect();
            vc.sort_unstable();
            (vc[0], vc[1], vc[2])
        })
        .collect()
}

pub fn part_one(input: &[(u32, u32, u32)]) -> u32 {
    let mut sum = 0;
    for (l, w, h) in input {
        sum += 2 * l * w + 2 * w * h + 2 * h * l + l * w;
    }
    sum
}

pub fn part_two(input: &[(u32, u32, u32)]) -> u32 {
    let mut sum = 0;
    for (l, w, h) in input {
        sum += l * 2 + w * 2 + l * w * h;
    }
    sum
}
