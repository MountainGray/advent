from advent import get_input, solution_timer
import re


@solution_timer(2015, 5, 1)
def part_one(input_data: list[str]):

    nice_strings = 0
    for line in input_data:
        qual = 0
        characters = set(line)

        vowels = ["a", "e", "i", "o", "u"]
        vowel_count = 0
        for vowel in vowels:
            vowel_count += line.count(vowel)
        if vowel_count >= 3:
            qual += 1

        bad_strs = ["ab", "cd", "pq", "xy"]
        for bad_str in bad_strs:
            if line.count(bad_str) >= 1:
                qual -= 1
                break
        for char in characters:
            if line.count(char + char) >= 1:
                qual += 1
                break
        if qual == 2:
            nice_strings += 1
    return nice_strings


@solution_timer(2015, 5, 2)
def part_two(input_data: list[str]):
    nice_string_count = 0

    for line in input_data:
        qual = 0
        char = set(line)
        for ch in char:
            regex = re.compile(f"{ch}.{ch}")
            if regex.search(line):
                qual += 1
                break

        done = False
        for ch in char:
            for ch2 in char:
                regex = re.compile(f"{ch}{ch2}")
                if len(regex.split(line)) > 2:
                    qual += 1
                    done = True
                    break
            if done:
                break

        if qual >= 2:
            nice_string_count += 1
    return nice_string_count


if __name__ == "__main__":
    input_data = get_input(2015, 5)
    part_one(input_data)
    part_two(input_data)
