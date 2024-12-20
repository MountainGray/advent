use regex::{self, Regex};
use std::collections::HashMap;

const MDIM: i32 = 71;

fn bfs(start: (i32, i32), grid: &[&[u8]], cost: &mut HashMap<(i32,i32), i32>) {
    let mut queue = vec![(start, 0)];
    while !queue.is_empty() {
        let ((x,y), c) = queue.pop().unwrap();
        if x < 0 || x >= MDIM || y < 0 || y >= MDIM || grid[y as usize][x as usize] == 1 {
            continue;
        }
        if let Some(c_low) = cost.get(&(x,y)) {
            if c >= *c_low {
                continue;
            } else {
                cost.insert((x,y), c);
            }
        } else {
            cost.insert((x,y), c);
        }
        queue.push(((x-1,y), c+ 1));
        queue.push(((x+1,y), c+ 1));
        queue.push(((x,y-1), c+ 1));
        queue.push(((x,y+1), c+ 1));
    }
}



fn part1(inp: &str) {
    let mut grid = [[0; MDIM as usize]; MDIM as usize];

    let nums = Regex::new(r"\d+").unwrap();
    let cords= inp.lines()
        .map(|l| nums.captures_iter(l).map(|m| m.extract()))
        .map(|f| )
    for i in 0..1024 {


    }





}

fn part2(inp: &str) {

}