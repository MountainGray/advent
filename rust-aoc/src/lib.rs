//extern crate advent_of_code_2024;
extern crate aoc_runner;

#[macro_use]
extern crate aoc_runner_derive;

pub mod day1;
pub mod day10;
pub mod day11;
//pub mod day12;
pub mod day13;
pub mod day14;
//pub mod day15;
pub mod day17;
pub mod day18;
pub mod day2;
pub mod day3;
pub mod day4;
pub mod day5;
pub mod day6;
pub mod day7;
pub mod day8;
pub mod day9;

aoc_lib! { year = 2024 }

/// Trait for extracting numbers from strings
pub trait NumberExtraction {
    /// Extracts all integers from a string
    ///
    /// # Examples
    /// ```
    /// use rust_aoc::NumberExtraction;
    ///
    /// let s = "The price is $42 and the quantity is 3.";
    /// assert_eq!(s.extract_numbers(), vec![42, 3]);
    ///
    /// let s = "No numbers here!";
    /// assert_eq!(s.extract_numbers(), Vec::<i32>::new());
    /// ```
    fn extract_numbers(&self) -> Vec<i32>;

    /// Extracts all unsigned integers from a string
    ///
    /// # Examples
    /// ```
    /// use rust_aoc::NumberExtraction;
    ///
    /// let s = "The price is $42 and the quantity is 3.";
    /// assert_eq!(s.extract_unsigned_numbers(), vec![42, 3]);
    ///
    /// let s = "Negative -42 should only get 42.";
    /// assert_eq!(s.extract_unsigned_numbers(), vec![42, 42]);
    /// ```
    fn extract_unsigned_numbers(&self) -> Vec<u32>;

    /// Extracts all floating-point numbers from a string
    ///
    /// # Examples
    /// ```
    /// use rust_aoc::NumberExtraction;
    ///
    /// let s = "The price is $42.50 and the temperature is -3.14.";
    /// assert_eq!(s.extract_floats(), vec![42.50, -3.14]);
    ///
    /// let s = "No numbers here!";
    /// assert_eq!(s.extract_floats(), Vec::<f64>::new());
    /// ```
    fn extract_floats(&self) -> Vec<f64>;
}

/// Implementation of NumberExtraction for String and &str
impl NumberExtraction for str {
    fn extract_numbers(&self) -> Vec<i32> {
        // Regex to match integers (positive and negative)
        let number_regex = regex::Regex::new(r"-?\d+").unwrap();

        number_regex
            .find_iter(self)
            .filter_map(|mat| mat.as_str().parse::<i32>().ok())
            .collect()
    }

    fn extract_unsigned_numbers(&self) -> Vec<u32> {
        // Regex to match only positive integers
        let number_regex = regex::Regex::new(r"\d+").unwrap();

        number_regex
            .find_iter(self)
            .filter_map(|mat| mat.as_str().parse::<u32>().ok())
            .collect()
    }

    fn extract_floats(&self) -> Vec<f64> {
        // Regex to match floating-point numbers (including scientific notation)
        let float_regex = regex::Regex::new(r"-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?").unwrap();

        float_regex
            .find_iter(self)
            .filter_map(|mat| mat.as_str().parse::<f64>().ok())
            .collect()
    }
}

// Implement for String type as well
impl NumberExtraction for String {
    fn extract_numbers(&self) -> Vec<i32> {
        self.as_str().extract_numbers()
    }

    fn extract_unsigned_numbers(&self) -> Vec<u32> {
        self.as_str().extract_unsigned_numbers()
    }

    fn extract_floats(&self) -> Vec<f64> {
        self.as_str().extract_floats()
    }
}

pub trait Grid<'a, T: 'a> {
    fn enum_grid(&'a self) -> impl Iterator<Item = (usize, usize, &'a T)>;
}

//impl Vec<&str> {}

impl<'a, T: 'a> Grid<'a, T> for Vec<Vec<T>> {
    fn enum_grid(&'a self) -> impl Iterator<Item = (usize, usize, &'a T)>
    where
        T: 'a,
    {
        self.iter()
            .enumerate()
            .flat_map(|(idy, l)| l.iter().enumerate().map(move |(idx, v)| (idx, idy, v)))
    }
}
