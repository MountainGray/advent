use std::error::Error;

fn main() {
    println!("Hello, world!");
    let st = std::env::current_dir().expect("msg");
    println!("{}", st.display());
}
