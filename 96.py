from functools import reduce
from itertools import chain, product

empty = '0'
all_symbols = '123456789'

def row(sudoku, r):
    return sudoku[9*r:9*(r+1)]

def col(sudoku, c):
    return [sudoku[9*r+c] for r in range(9)]

def box(sudoku, b):
    br, bc = b//3, b%3
    return [sudoku[3*(9*br+bc)+9*r+c] for r, c in product(range(3), repeat=2)]

def check(sudoku):
    def check_set(symbols):
        seen = set()
        for symbol in symbols:
            if symbol is not empty:
                if symbol in seen:
                    return False
                seen.add(symbol)
        return True
    for symbols in chain([row(sudoku, r) for r in range(9)],
                         [col(sudoku, c) for c in range(9)],
                         [box(sudoku, b) for b in range(9)]):
        if not check_set(symbols):
            return False
    return True

def solve(sudoku, i=0):
    # if i is out of range, we're done
    if i >= len(sudoku):
        return sudoku
    # if i is a given, move on
    if sudoku[i] is not empty:
        return solve(sudoku, i+1)
    # try every possibility for i, recursively
    for symbol in all_symbols:
        sudoku[i] = symbol
        if check(sudoku):
            guess = solve(sudoku, i+1)
            if guess:
                return guess
    # if none of them worked out, reset i and report the failure
    sudoku[i] = empty
    return None

def parse(grid_string):
    return list(''.join(grid_string))

def pretty(sudoku):
    return ''.join([''.join(sudoku[9*r:9*(r+1)]) + '\n' for r in range(9)])

if __name__ == '__main__':
    # This file has sudokus in grid string form that parse() likes, punctuated
    # by header lines.
    input = open('p096_sudoku.txt').read().split('\n')[:-1]
    grid_strings = [input[i+1:i+10] for i in range(0, len(input), 10)]
    for grid_string in grid_strings:
        unsolved = parse(grid_string)
        solved = solve(unsolved)
        print(pretty(solved))
