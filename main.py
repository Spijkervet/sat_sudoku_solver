#!/usr/bin/python

import argparse
import pycosat
from reader import CNF_Reader
from converter import Sudoku_CNF
from grid import create_grid, print_grid
from pprint import pprint
import time
import os

from solver import Solver

def main(sudoku, sudoku_rules, strategy):

    if sudoku_rules:
        clauses = sudoku_rules.clauses + sudoku.clauses
        variables = sudoku_rules.variables | sudoku.variables
    else:
        clauses = sudoku.clauses
        variables = sudoku.variables

    solver = Solver(strategy, clauses, variables)
    start_time = time.time()
    solution = solver.solve()
    print("EXECUTION TIME: {}".format(time.time() - start_time))

    # solution = set(pycosat.solve(merged.clauses))
    if solution is False:
        print("No solution found")
    else:
        print("Solution found!")
        # print(solver.clauses.clauses)
        print("SOLUTION", len(solution))
        grid = create_grid(solution)
        print("SPLITS", solver.splits)
        pprint(grid)

        # true_assignments = [v for key, v in solver.assignments.items() if v.assigned == True]
        # print('true ass', len(true_assignments))

    print("### YOUR SUDOKU ###")
    print("VARIABLES: {}".format(sudoku.num_variables))
    print("CLAUSES: {}".format(len(sudoku.clauses)))
    print("")



if __name__ == '__main__':
    print("SAT SUDOKU SOLVER")
    print("_______________________\n")

    parser = argparse.ArgumentParser(description='SAT solver for Sudoku')
    parser.add_argument('input_file', help='Input file')
    parser.add_argument('-S', help='Strategy')
    p = parser.parse_args()
    strategy = p.S



    print("### STRATEGY: {} ###".format(strategy))
    print("")

    if os.path.splitext(p.input_file)[1][1:].strip().lower() == 'txt':
        sudoku_rules = CNF_Reader()
        sudoku_rules.read('./cnf/sudoku-rules.cnf')
        print("### SUDOKU RULES ###")
        print("VARIABLES: {}".format(sudoku_rules.num_variables))
        print("CLAUSES: {}".format(len(sudoku_rules.clauses)))
        print("")

        sud_conv = Sudoku_CNF()
        conv = sud_conv.convert(p.input_file)
        for c in conv:
            sudoku = CNF_Reader()
            sudoku.read_string(c)
            main(sudoku, sudoku_rules, strategy)
    else:
        cnf = CNF_Reader()
        cnf.read(p.input_file)
        main(cnf, None, strategy)

