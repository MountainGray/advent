'''
Different somewhat generic helper functions and structures
who needs clean namespaces anyway
'''

# Imports

from typing import List, Tuple, Dict, Set, Union, Any, Annotated
from itertools import *
from collections import defaultdict


# Strucutres

text_number_tr = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five" : 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

number_text_tr = {value: key for key, value in text_number_tr.items()}

# Functions

def print_grid(grid):
    '''Prints out a 2D grid, no assumptions about the value type'''
    for i in grid:
        print(i)