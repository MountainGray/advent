import os
from typing import Any, Callable, List

import requests
from advent.config import ROOT_DIR
from advent.console import console


def get_input(year, day, filename="input.txt", split_char = "\n", remove_end_blank=True) -> List[str]:
    """
    Load the input, returns a list of strings
    TODO: add load input if not found
    Args:
        year: year of the puzzle
        day: day of the puzzle
        filename: filename of the input
        remove_end_blank: remove the empty line at the end of the file (default: True)
    """
    path: str = get_input_path(year, day, filename)
    if not os.path.exists(path):
        if filename == "input.txt":
            _download_input(year, day)
        else:
            raise FileNotFoundError(f"{path} does not exist")

    with open(path, "r") as f:
        contents = f.read()
        if contents == "Puzzle inputs differ by user.  Please log in to get your puzzle input.":
            _download_input(year, day)
            return get_input(year, day, filename, split_char, remove_end_blank)
        if (
            contents[-1] == "\n" and remove_end_blank
        ):  # Catch those pesky blank lines at the end
            contents= contents.removesuffix("\n")
        contents = contents.split(split_char)
        return contents


def get_input_grid(
    year,
    day,
    map_func: Callable[[str], Any],
    delim: str = "",
    filename="input.txt",
    remove_end_blank=True,
) -> List[List[str]] | List[List[Any]]:
    """
    Load the input, returns a list of lists(grid) of strings,
     or whatever the map_func returns
    Args:
        year: year of the puzzle
        day: day of the puzzle
        map_func: function to map the string to something else
        delim: delimiter to split the input
        filename: filename of the input
        remove_end_blank: remove the empty line at the end of the file
    """
    contents = get_input(year, day, filename, remove_end_blank=remove_end_blank)
    if delim == "":
        grid = [[x for x in line] for line in contents]
    else:
        grid = [[x for x in line.split(delim)] for line in contents]

    if map_func:
        grid = [[map_func(x) for x in line] for line in grid]

    return grid


def get_input_path(year, day, filename="input.txt") -> str:
    return os.path.join(ROOT_DIR, f"input/{year}/day{day}/{filename}")



def _download_input(year, day):
    "downloads the input for a given day from adventofcode.com"
    
    cookie_path = ROOT_DIR + "/input/.cookie"

    if not os.path.exists(ROOT_DIR + "/input"):
        os.mkdir(ROOT_DIR + "/input")

    if not os.path.exists(cookie_path):
        session_cookie = console.input(
            "Session cookie missing, please input adventofcode.com session cookie: "
        )
        with open(cookie_path, "w", encoding="utf-8") as file:
            file.write(session_cookie)

    cookie = open(cookie_path, "r", encoding="utf-8").read().split("\n")[0]
    headers = {
        "session": cookie,
        "User-Agent": "github.com/jacobgnewman/advent/tree/master/python-aoc/advent_utils by jacobgnewman001@gmail.com",
        }
    url = f"https://adventofcode.com/{year}/day/{day}/input"

    session = requests.Session()
    response = session.get(url, cookies=headers)

    # Response if challenge is not unlocked yet (make prefetch cli command?)
    # TODO: check if this is the correct response
    if response.text == "Please don't repeatedly request this endpoint before it unlocks!":
        console.print(
            f"Day {day} has not unlocked yet, please try again later", style="red"
        )
        return # TODO: raise exception? Some form of error state

    # response if session cookie invalid
    if response.text == "Puzzle inputs differ by user.  Please log in to get your puzzle input.\n":
        console.print("Likely invalid session cookie, please input new session cookie", style="red")
        session_cookie = console.input()
        with open(cookie_path, "w", encoding="utf-8") as file:
            file.write(session_cookie)
        return _download_input(year, day)

    if not os.path.exists(f"{ROOT_DIR}/input/{year}/day{day}"):
        os.makedirs(f"{ROOT_DIR}/input/{year}/day{day}")
    

    with open(f"{ROOT_DIR}/input/{year}/day{day}/input.txt", "w", encoding="utf-8") as file:
        file.write(response.text)
