use rustaoc::load_input_str;

fn main() {
    let input = load_input_str(2019, 1);
    let inputvec = input.split("\n").map(|x| x.parse::<u32>().unwrap());
    let mut total1 = 0;
    let mut total2 = 0;
    for inp in inputvec {
        total1 += p1(inp);
        total2 += p2(inp);
    }
    println!("P1:{} P2:{}", total1, total2);
}

fn p1(val: u32) -> u32 {
    val / 3 - 2
}

fn p2(mut val: u32) -> u32 {
    let mut tot = 0;
    while val > 8 {
        val = val / 3 - 2;
        tot += val;
    }
    tot
}
