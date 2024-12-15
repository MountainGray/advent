use std::collections::hash_map;
use std::collections::HashMap;
use std::collections::HashSet;

fn are_neigbour(p1: (usize, usize), p2: (usize, usize)) -> bool {
    let (x, y) = p1;
    let (a, b) = p2;
    x.abs_diff(a) + y.abs_diff(b) == 1
}

#[aoc(day12, part1)]
pub fn part1(input: &str) -> usize {
    let grid: Vec<Vec<char>> = input.lines().map(|l| l.chars().collect()).collect();
    let mut vpos: HashMap<char, HashSet<(usize, usize)>> = HashMap::new();

    for (idy, l) in grid.iter().enumerate() {
        for (idx, c) in l.iter().enumerate() {
            if vpos.contains_key(c) {
                vpos.get_mut(c).unwrap().insert((idx, idy));
            } else {
                let ns = HashSet::new();
                ns.insert((idx, idy));
                vpos.insert(*c, ns);
            }
        }
    }

    let mut ans = 0;
    for (_, mut s) in vpos {
        while !s.is_empty() {
            let mut a = 1;
            let mut p = 4;
            let fv = s.iter().take(1);
            let mut vg = vec![fv];
            loop {
                let mut rl = vec![];
                for j in s.iter() {
                    let mut c = 0;
                    for k in vg.iter() {
                        if are_neigbour(*j, *k) {
                            c += 1;
                        }
                        if c == 3 {
                            break;
                        };
                    }
                    if c > 0 {
                        rl.push(j);
                        a += 1;
                        p += 3 - c;
                    }
                }
                if rl.len() == 0 {
                    break;
                } else {
                    vg.extend(rl);
                }
            }
            ans += a * p;
        }
    }

    ans
}

//#[aoc(day12, part2)]
//pub fn part2(input: &str) -> u64 {
//}
