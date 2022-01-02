use std::fs;

pub fn load_input_str(year: i32, day: i32)-> String{
    let filepath = format!("input/{}{:02}.txt",year,day);
    let input = fs::read_to_string(filepath)
        .expect("error reading file");
    input
}
// pub fn input_split_newline(year: i32, day: i32)-> Vec<&str>{
//     let filepath = format!("input/{}{:02}.txt",year,day);
//     let input = fs::read_to_string(filepath)
//         .expect("error reading file");
//     let split = input.split("\n").collect::<Vec<&str>>();
//     split
// }