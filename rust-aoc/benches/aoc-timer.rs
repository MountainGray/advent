use aoc_util::day_input;
use criterion::{black_box, criterion_group, criterion_main, Criterion};
use rust_aoc::day1;
use rust_aoc::day2;

pub fn day1_bench(c: &mut Criterion) {
    let inp = day_input(2024, 1);
    c.bench_function("day 1 part 1", |b| b.iter(|| black_box(day1::part1(&inp))));
    c.bench_function("day 1 part 2", |b| b.iter(|| black_box(day1::part2(&inp))));
}

pub fn day2_bench(c: &mut Criterion) {
    let inp = day_input(2024, 2);
    c.bench_function("day 2 part 1", |b| b.iter(|| black_box(day2::part1(&inp))));
    c.bench_function("day 2 part 2", |b| b.iter(|| black_box(day2::part2(&inp))));
}

criterion_group!(benches, day1_bench);
criterion_group!(benches, day2_bench);
criterion_main!(benches);
