use rustaoc::load_input_str;

fn main() {
    let input = load_input_str(2019, 1);
    let inputvec = input.split("\n").collect::<Vec<&str>>();
    p1(&inputvec);
    p2(&inputvec);
}

fn p1(modules: &Vec<&str>) {
    let mut fuel = 0;
    for module in modules {
        let weight = module.parse::<i32>().unwrap();
        fuel += weight / 3 - 2;
    }
    println!("P1: {}", fuel);
}
fn p2(modules: &Vec<&str>) {
    let mut fuel = 0;
    for module in modules {
        let mut weight: i32 = module.parse::<i32>().unwrap();
        while weight > 8 {
            weight = weight / 3 - 2;
            fuel += weight;
        }
    }
    println!("P2: {}", fuel);
}
