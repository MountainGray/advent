use rustaoc::load_input_str;

fn main() {
    let input = inputparse();
    let p1 = p1(input.clone(),12,2);
    println!("{}", p1);
    p2(input);
}

fn inputparse() -> Vec<usize> {
    let inputstr = load_input_str(2019, 2);
    let ints = inputstr.split(",").collect::<Vec<&str>>();
    let mut memory = Vec::new();
    for int in ints {
        memory.push(int.parse::<usize>().unwrap());
    }
    memory
}

fn p1(mut memory: Vec<usize>, x:usize, y:usize)->usize {
    let mut idx: usize = 0;
    let max = memory.len();
    memory[1] = x;
    memory[2] = y;
    loop {
        if memory[idx] == 99 {
            break;
        } else {
            let mod_pos = memory[idx + 3];
            if mod_pos >= max {
                break;
            }
            let a = memory[idx + 1];
            let b = memory[idx + 2];
            if memory[idx] == 1 {
                memory[mod_pos] = memory[a] + memory[b];
            } else {
                memory[mod_pos] = memory[a] * memory[b];
            }
        }
        idx += 4;
    }
    memory[0]
}

fn p2(memory: Vec<usize>) {
    for x in 0..100 {
        for y in 0..100 {
            if p1(memory.clone(),x,y) == 19690720 {
                println!("{}", 100 * x + y);
                return;
            }
        }
    }
}
