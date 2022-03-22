import os
from typing import Any, List, Callable
from advent.config import ROOT_DIR


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
    path: str = _get_input_path(year, day, filename)
    if not os.path.exists(path):
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


def _get_input_path(year, day, filename="input.txt") -> str:
    return os.path.join(ROOT_DIR, f"input\\{year}\\day{day}\\{filename}")
