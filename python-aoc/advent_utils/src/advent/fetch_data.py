"Utils for loading puzzle input"
import os
import requests

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

    with open(f"input/{year}/day{day}.txt", "w") as f:
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
