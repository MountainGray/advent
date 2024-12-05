use aoc_util::day_input;
use criterion::{black_box, criterion_group, criterion_main, Criterion};
use rust_aoc::day4;

pub fn day1_bench(c: &mut Criterion) {
    let inp = day_input(2024, 4);
    c.bench_function("day 4 part 1", |b| b.iter(|| black_box(day4::part1(&inp))));
    c.bench_function("day 4 part 2", |b| b.iter(|| black_box(day4::part2(&inp))));
}

criterion_group!(benches, day1_bench);
criterion_main!(benches);
