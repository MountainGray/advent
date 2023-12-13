'''
Different somewhat generic helper functions and structures
who needs clean namespaces anyway
'''

# Imports

from typing import List, Tuple, Dict, Set, Union, Any, Annotated, Iterator
from itertools import product
from collections import defaultdict
from pprint import pprint


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

def iter_neigbours(dim: int) -> List[Tuple[int,...]]:
    '''Returns a list of neighbours cells for a given grid of n dimensions'''
    return list(product([-1, 0, 1], repeat=dim))

def grid_neigbours(pos: Tuple[int, ...]) -> List[Tuple[int,...]]:
    '''Returns a list of neighbours for a given position in a n dim grid'''
    neigbours = [tuple(map(sum, zip(pos, i))) for i in iter_neigbours(len(pos))]
    neigbours.remove(pos) # remove self
    return  neigbours

def transform_grid(grid: List[List[Any]] ) -> List[List[Any]]:
    '''Transforms a grid'''
    return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
