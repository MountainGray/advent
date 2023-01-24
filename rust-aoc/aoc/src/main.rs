mod manager;
fn main() {
    println!("{}",manager::get_input(2017, 2));
    println!("{}",manager::get_input_directory(2017, 2).display());
}
