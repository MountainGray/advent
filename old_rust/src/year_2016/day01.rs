fn solve(input: &str) -> i32 {
    let (mut x, mut y) = (0, 0);
    let mut dir = (0, 1);
    let directions = input.split(", ").filter_map(|d| {
        let (dir, num) = d.split_at(1);
        let dist = num.parse::<i32>().ok()?;
        Some((dir, dist))
    });

    for (r, d) in directions {
        ()
    }

    return 4;
}
