import os
from typing import Any, List, Callable
from advent.config import ROOT_DIR
import requests
from advent.console import console


def get_input(year, day, filename="input.txt", remove_end_blank=True) -> List[str]:
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
        contents = f.read().split("\n")
        if (
            contents[-1] == "" and remove_end_blank
        ):  # Catch those pesky blank lines at the end
            contents.pop()
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
    contents = get_input(year, day, filename, remove_end_blank)
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
    headers = {"session": cookie}
    url = f"https://adventofcode.com/{year}/day/{day}/input"

    session = requests.Session()
    response = session.get(url, cookies=headers)
    if not os.path.exists(f"{ROOT_DIR}/input/{year}/day{day}"):
        os.makedirs(f"{ROOT_DIR}/input/{year}/day{day}")

    with open(f"{ROOT_DIR}/input/{year}/day{day}/input.txt", "w", encoding="utf-8") as file:
        file.write(response.text)
