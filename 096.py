from itertools import product

empty = '0'
all_symbols = '123456789'

def neighborhood(sudoku, i):
    """
    Given a sudoku as a [char; 81] and an index i, return a set containing
    every value that occurs in i's row, column, or box in the sudoku.
    """
    row, col = i//9, i%9
    box = row//3*3 + col//3
    return {sudoku[row*9 + c] for c in range(9)} | \
           {sudoku[r*9 + col] for r in range(9)} | \
           {sudoku[3*(box//3*9 + box%3) + r*9 + c] for r, c in product(range(3), repeat=2)}

def best_branch(sudoku):
    """
    Given a sudoku as a [char; 81], return the index of the empty spot whose
    possible values are most restricted, along with its set of possible
    values. If there are no empty spots, return None in lieu of an index.
    Possible values are computed by eliminating every value occuring in an
    index's neighborhood (see above).
    """
    best_index, best_choices = None, set(all_symbols)
    for i in range(len(sudoku)):
        if sudoku[i] is not empty:
            continue
        choices = set(all_symbols) - neighborhood(sudoku, i)
        if len(choices) < len(best_choices):
            best_index, best_choices = i, choices
    return best_index, best_choices

def solve(sudoku):
    """
    Given a sudoku as a [char; 81], return a solved version of it, or None
    if it is impossible to solve. Obviously, for every non-empty spot in the
    input, that spot in the output has the same value; the output has no
    empty spots; and the output is a valid sudoku.
    The input is altered: if the sudoku is solvable, the input is transformed
    into the solved output and returned. If None is returned, then the input
    is returned to its original state first.
    """
    index, choices = best_branch(sudoku)
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
