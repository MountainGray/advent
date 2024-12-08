const WALL: u8 = b'#';
const G: u8 = b'^';
const N: usize = 130;

// functional p1?

// TODO: Change accept from enter to tab jacob...
use std::collections::HashSet;

// TODO make translation on raw bytes including newlines...
#[aoc(day6, part1)]
pub fn part1(input: &str) -> usize {
    let inp = input.as_bytes();
    let mut guard: (i32, i32) = (0, 0);
    let mut dx = 0;
    let mut dy = -1;

    for y in 0..N {
        for x in 0..N {
            if inp[y * (N + 1) + x] == G {
                guard = (x as i32, y as i32);
            }
        }
    }
    // TODO: eval set for visited, or modifying the array...

    let mut visited: HashSet<(i32, i32)> = HashSet::new();
    loop {
        // visited.insert(guard);
        let (gx, gy) = guard;
        let (nx, ny) = (gx + dx, gy + dy);
        if nx < 0 || nx as usize >= N || ny < 0 || ny as usize >= N {
            break;
        }
        let c = inp[(ny as usize) * (N + 1) + nx as usize];
        if c != WALL {
            if c != b'x' {
                //inp[(ny as usize) * (N + 1) + nx as usize] = b'x';
                visited.insert((nx, ny));
                //ans += 1;
            }
            guard = (nx, ny);
        } else {
            (dx, dy) = (-dy, dx);
            //dir = (dir + 1) % 4;
        };
    }
    visited.len()
}

// TODO make translation on raw bytes including newlines...
#[aoc(day6, part2)]
pub fn part2(input: &str) -> usize {
    let inp = input.as_bytes();
    let mut guard: (i32, i32) = (0, 0);
    let mut dx = 0;
    let mut dy = -1;

    for y in 0..N {
        for x in 0..N {
            if inp[y * (N + 1) + x] == G {
                guard = (x as i32, y as i32);
            }
        }
    }

    let mut grid: Vec<Vec<u8>> = input.lines().map(|l| l.bytes().collect()).collect();
    // TODO: eval set for visited, or modifying the array...
    let mut answer = 0;

    let mut visited: HashSet<(i32, i32)> = HashSet::new();
    loop {
        visited.insert(guard);
        let (gx, gy) = guard;
        let (nx, ny) = (gx + dx, gy + dy);

        if nx < 0 || nx as usize >= grid.len() || ny < 0 || ny as usize >= grid.len() {
            break;
        }
        if grid[ny as usize][nx as usize] != WALL {
            // try to find loop :)
            if !visited.contains(&(nx, ny)) {
                grid[ny as usize][nx as usize] = b'#';

                let mut ndir = dir;
                let mut looped: HashSet<((i32, i32), usize)> = HashSet::new();
                let mut found = false;
                let mut nguard = guard;
                loop {
                    if looped.contains(&(nguard, ndir)) {
                        found = true;
                        break;
                    } else {
                        looped.insert((nguard, ndir));
                    }
                    let (gx, gy) = nguard;
                    let (nx, ny) = (gx + DX[ndir], gy + DY[ndir]);
                    if nx < 0 || nx as usize >= grid.len() || ny < 0 || ny as usize >= grid.len() {
                        break;
                    }
                    if grid[ny as usize][nx as usize] != WALL {
                        nguard = (nx, ny);
                    } else {
                        ndir = (ndir + 1) % 4;
                    }
                }

                if found {
                    answer += 1;
                }

                grid[ny as usize][nx as usize] = b'.';
            }

            guard = (nx, ny);
        } else {
            dir = (dir + 1) % 4;
        };
    }
    answer
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        let s = "....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
";
        assert_eq!(part1(s), 6);
    }
}
