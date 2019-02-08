#!/usr/bin/python
import argparse
from reader import CNF_Reader


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='SAT solver for Sudoku')
    parser.add_argument('input_file', help='Input file')
    parser.add_argument('-S', help='Strategy')
    p = parser.parse_args()

    cnf_reader = CNF_Reader()
    cnf_reader.read(p.input_file)

    print(cnf_reader.num_variables)
    print(cnf_reader.clauses)

    strategy = p.S
    print("### STRATEGY: {} ###".format(strategy))
