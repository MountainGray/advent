"Utils for loading puzzle input"
import os
import requests
import fire

def get_input(year, day):
    "downloads the input for a given day from adventofcode.com"

    if not os.path.exists("credentials.txt"):
        print("Please create a credentials.txt file with your advent of code session cookie")
        return

    cookie = open("credentials.txt", "r").read().split("\n")[0]
    headers = {'session': cookie}
    url = f'https://adventofcode.com/{year}/day/{day}/input'

    session = requests.Session()
    response = session.get(url,cookies=headers)

    with open(f"input/{year}/day{day}/input.txt", "w") as f:
        f.write(response.text)

def load_input(year,day, delimiter="\n", sub_delimiter=None, map_func=None):
    input_path = f"input/{year}/day{day}/input.txt"
    if not os.path.exists(input_path):
        get_input(year, day)
        
    with open(input_path,'r') as f:
        if map_func and sub_delimiter :
            return [list(map(map_func, line.split(sub_delimiter))) for line in f.readlines()]
        if map_func and not sub_delimiter:
            return [map_func(line) for line in f.readlines()]
        elif not map and sub_delimiter:
            return [line.split(sub_delimiter) for line in f.readlines()] 
        else:
            return f.read().split(delimiter)


# creates input directories up to the given year
def make_input_folders():
    import time
    year_start = 2015
    year_current = time.localtime().tm_year
    for year in range(year_start, year_current+ 1):
        for day in range(1, 25):
            path = f"input/{year}/day{day}"
            if not os.path.exists(path):
                os.makedirs(path)

def get_all_input():
    import time
    year_start = 2015
    year_current = time.localtime().tm_year
    for year in range(year_start, year_current):
        for day in range(1, 25):
            get_input(year, day)


if __name__ == "__main__":
    import fire
    fire.Fire()
