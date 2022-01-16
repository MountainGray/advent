use rustaoc::load_input_str;

fn main() {
    let input = inputparse();
    p1(input.clone());
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

fn p1(mut memory: Vec<usize>) {
    let mut idx: usize = 0;
    memory[1] = 12;
    memory[2] = 2;
    loop {
        println!("{:?}",memory);
        if memory[idx] == 99 {
            break;
        } else {
            let mod_pos = memory[idx + 3];
            let a = memory[idx + 1];
            let b = memory[idx + 2];
            println!("idx {} a {} b {} mod_pos {}", idx, a, b, mod_pos);
            if memory[idx] == 1 {
                memory[mod_pos] = memory[a] + memory[b];
            } else {
                memory[mod_pos] = memory[a] * memory[b];
            }
        }
        idx += 4;
    }
    println!("{}", memory[0]);
}

fn p1(mut memory: Vec<usize>) {
    let mut idx: usize = 0;
    memory[1] = 12;
    memory[2] = 2;
    loop {
        println!("{:?}",memory);
        if memory[idx] == 99 {
            break;
        } else {
            let mod_pos = memory[idx + 3];
            let a = memory[idx + 1];
            let b = memory[idx + 2];
            println!("idx {} a {} b {} mod_pos {}", idx, a, b, mod_pos);
            if memory[idx] == 1 {
                memory[mod_pos] = memory[a] + memory[b];
            } else {
                memory[mod_pos] = memory[a] * memory[b];
            }
        }
        idx += 4;
    }
    println!("{}", memory[0]);
}
}