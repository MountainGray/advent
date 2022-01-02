use rustaoc::load_input_str;

fn main() {
    let input = inputparse();
    p1(input)

}

fn inputparse() -> Vec<i32>{
    let inputstr = load_input_str(2019, 2);
    let ints = inputstr.split(",").collect::<Vec<&str>>();
    let mut memory = Vec::new();
    for int in ints {
        memory.push(int.parse::<i32>().unwrap())
    }
    println!("{:?}",memory)
    memory
}

fn p1(memory: Vec<i32>){

}

