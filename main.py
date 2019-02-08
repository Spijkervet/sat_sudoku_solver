#!/usr/bin/python

import argparse
# import pycosat
from reader import CNF_Reader
from converter import Sudoku_CNF
from grid import create_grid, print_grid
from pprint import pprint

from solver import Solver

if __name__ == '__main__':
    print("SAT SUDOKU SOLVER")
    print("_______________________\n")

    parser = argparse.ArgumentParser(description='SAT solver for Sudoku')
    parser.add_argument('input_file', help='Input file')
    parser.add_argument('-S', help='Strategy')
    p = parser.parse_args()
    strategy = p.S


    sudoku_rules = CNF_Reader()
    sudoku_rules.read('./cnf/sudoku-rules.cnf')
    print("### SUDOKU RULES ###")
    print("VARIABLES: {}".format(sudoku_rules.num_variables))
    print("CLAUSES: {}".format(len(sudoku_rules.clauses)))
    print("")

    print("### STRATEGY: {} ###".format(strategy))
    print("")

    solver = Solver(strategy)

    sud_conv = Sudoku_CNF()
    sud_conv.convert(p.input_file)
    for c in sud_conv.convert(p.input_file):
        sudoku = CNF_Reader()
        sudoku.read_string(c)

        clauses = sudoku_rules.clauses + sudoku.clauses

        solution = solver.solve(clauses)
        # solution = set(pycosat.solve(clauses))
        if solution is None:
            print("No solution found")
        else:
            grid = create_grid(solution)

        print("### YOUR SUDOKU ###")
        print("VARIABLES: {}".format(sudoku.num_variables))
        print("CLAUSES: {}".format(len(sudoku.clauses)))
        print("")
        # print_grid(grid)
