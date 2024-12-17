use lazy_static::lazy_static;
use rayon::prelude::*;
use std::{u32, u64};

lazy_static! {
    static ref instrs: [u64; 16] = [2, 4, 1, 5, 7, 5, 1, 6, 4, 2, 5, 5, 0, 3, 3, 0];
}

const SIZE: usize = 16;

fn sol(i: u64) -> u64 {
    if i % 10_000_000 == 0 {
        println!("{}", i);
    };
    let mut vs = [i, 0, 0]; // vs[0] = A, vs[1] = B, vs[2] = C
    let mut ip = 0; // Instruction pointer
    let mut out: [u64; SIZE] = [0; SIZE];
    let mut out_idx = 0;

    while ip < instrs.len() {
        let mut js = false; // Jump flag
        let op = instrs[ip];
        let rand = instrs[ip + 1];

        // Determine the combo value
        let combo = match rand {
            0..=3 => rand,
            4 => vs[0], // A
            5 => vs[1], // B
            6 => vs[2], // C
            _ => unreachable!(),
        };

        // Perform the operation based on `op`
        match op {
            0 => {
                let denom = 2_u64.pow(combo as u32);
                vs[0] /= denom; // A = A / (2^combo)
            }
            1 => {
                vs[1] ^= rand; // B = B ^ rand
            }
            2 => {
                vs[1] = combo % 8; // B = combo % 8
            }
            3 => {
                if vs[0] != 0 {
                    js = true;
                    ip = rand as usize; // Jump to the value of rand
                }
            }
            4 => {
                vs[1] ^= vs[2]; // B = B ^ C
            }
            5 => {
                out[out_idx] = combo % 8;
                if out != instrs[..out_idx] {
                    return 0; // If output doesn't match, return false
                }
                out_idx += 1;
                if out_idx > SIZE {
                    return 0;
                }
            }
            6 => {
                let denom = 2_u64.pow(combo as u32);
                vs[1] = vs[0] / denom; // B = A / (2^combo)
            }
            7 => {
                let denom = 2_u64.pow(combo as u32);
                vs[2] = vs[0] / denom; // C = A / (2^combo)
            }
            _ => {}
        }
        if !js {
            ip += 2;
        }
    }
    if out_idx == 15 && out.iter().enumerate().all(|(idx, v)| *v == instrs[idx]) {
        i
    } else {
        0
    }
}

pub fn part1() {
    let x = (1490000000..u64::MAX)
        .into_par_iter()
        .map(sol)
        .find_any(|x| *x != 0)
        .unwrap();
    println!("TRY {x}");
}
