from itertools import product

empty = '0'
all_symbols = '123456789'

def neighborhood(sudoku, i):
    row, col = i//9, i%9
    box = row//3*3 + col//3
    rowset = set(sudoku[row*9 : (row+1)*9])
    colset = set([sudoku[r*9 + col] for r in range(9)])
    boxset = set([sudoku[3*(box//3*9 + box%3) + r*9 + c] for r, c in product(range(3), repeat=2)])
    return rowset | colset | boxset

def best_branch(sudoku):
    best_choices, best_index = set(all_symbols), None
    for i in range(len(sudoku)):
        if sudoku[i] is not empty:
            continue
        choices = set(all_symbols) - neighborhood(sudoku, i)
        if len(choices) < len(best_choices):
            best_choices, best_index = choices, i
    return best_choices, best_index

def solve(sudoku):
    choices, index = best_branch(sudoku)
    if index is None:
        return sudoku
    for symbol in choices:
        sudoku[index] = symbol
        solution = solve(sudoku)
        if solution:
            return solution
    sudoku[index] = empty
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
    print(sum(map(lambda sol: int(''.join(sol[:3])), map(pretty, map(solve, map(parse, grid_strings))))))
