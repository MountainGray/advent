use core::fmt;
use std::fmt::{Display, write};

mod manager;

pub fn day_input(year: u16, day: u8) -> String {
    manager::get_input(year, day)
}

pub enum AOCResult {
    String(String),
    Number(i64)
}

impl fmt::Display for AOCResult {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
       match self {
            AOCResult::String(string) => write(f, format_args!("{}", string)),
            AOCResult::Number(num) => write(f, format_args!("{}", num)),
       } 
    }
}