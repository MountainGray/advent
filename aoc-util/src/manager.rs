use chrono::Datelike;
use dotenv::dotenv;
use std::env;
use std::{fs, path::PathBuf};

fn get_input_path(year: u16, day: u8) -> PathBuf {
    let mut path = std::env::current_dir().expect("Can't fetch current dir");
    path.push(format!("input/{}/day{:02}/input.txt", year, day));
    path
}

fn get_input_directory(year: u16, day: u8) -> PathBuf {
    let mut path = std::env::current_dir().expect("Can't fetch current dir");
    path.push(format!("input/{}/day{:02}/", year, day));
    path
}

// Fetches the puzzle input for a given day
// Will cache puzzle input once retrieved locally
// NOTE: Relies on a valid sesssion cookie in input/aoc.session
pub fn get_input(year: u16, day: u8) -> String {
    let inp_path = get_input_path(year, day);
    if inp_path.exists() {
        fs::read_to_string(inp_path).expect("Failed to read from input file")
    } else {
        load_input(year, day)
    }
}

fn fetch_aoc_input(year: u16, day: u8) -> Result<String, Box<dyn std::error::Error>> {
    // Load environment variables from .env file
    dotenv().ok();

    // Get AOC session cookie from environment variable
    let session_cookie =
        env::var("AOC_SESSION_COOKIE").expect("AOC_SESSION_COOKIE must be set in .env file");

    //User-Agent=github.com/jacobgnewman/advent/ by jacobgnewman001@gmail.com

    // Create a client with the session cookie
    let client = reqwest::blocking::Client::new();
    let response = client
        .get(format!(
            "https://adventofcode.com/{}/day/{}/input",
            year, day
        ))
        .header("Cookie", format!("session={}", session_cookie))
        .send()?
        .text()?;

    Ok(response)
}

fn load_input(year: u16, day: u8) -> String {
    let directories = get_input_directory(year, day);
    fs::create_dir_all(directories).expect("Failed to make directiories");
    //println!("Making request to {} with cookie: {}", input_url, cookie);

    match fetch_aoc_input(year, day) {
        Ok(input) => {
            let path = get_input_path(year, day);
            fs::write(path.clone(), input).expect("Failed to write to file");
            fs::read_to_string(path).expect("Failed to read from file")
        }
        Err(e) => {
            panic!("Failed to get a response: {}", e)
        }
    }
}

struct DayInput {
    day: u32,
    input: String,
}

struct YearInput {
    year: u32,
    days: [Option<DayInput>; 26],
    day: u32,
}

fn detect_input(year: i32) -> Option<YearInput> {
    let ctime = chrono::Local::now();
    let y = ctime.year();
    None
}
