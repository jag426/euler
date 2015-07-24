from functools import reduce
from itertools import product

empty = '0'
symbols = '123456789'

def check(sudoku):
    def check_set(squares):
        seen = set()
        for square in squares:
            if square is not empty:
                if square in seen:
                    return False
                seen.add(square)
        return True
    for row in [sudoku[9*r:9*(r+1)] for r in range(9)]:
        if not check_set(row):
            return False
    for col in [[sudoku[9*r+c] for r in range(9)] for c in range(9)]:
        if not check_set(col):
            return False
    for block in [[sudoku[9*3*br+9*r+3*bc+c] for r, c in product(range(3), repeat=2)] for br, bc in product(range(3), repeat=2)]:
        if not check_set(block):
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
    for symbol in symbols:
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
    #for grid_string in grid_strings:
    #    unsolved = parse(grid_string)
    #    solved = solve(unsolved)
    #    print(pretty(solved))
    print(sum(map(lambda s: int(''.join(s[:3])), map(solve, map(parse, grid_strings)))))
