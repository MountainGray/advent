use aoc_util::day_input;
use criterion::{black_box, criterion_group, criterion_main, Criterion};
use rust_aoc::day1::{part1, part2, parse};

pub fn criterion_benchmark(c: &mut Criterion) {
    let inp = day_input(2024, 1);
    c.bench_function("day 1 part 1", |b| b.iter(|| black_box(part1(&inp))));
    c.bench_function("day 1 part 2", |b| b.iter(|| black_box(part2(&inp))));
    //c.bench_function("day 1 parse", |b| b.iter(|| black_box(parse(&inp))));
}

criterion_group!(benches, criterion_benchmark);
criterion_main!(benches);
