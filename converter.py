import os

CONVERTED_DIR = 'converted'

class Sudoku_CNF():

    def __init__(self):
        pass

    def convert(self, file_name):
        with open(file_name, 'r') as f:
            lines = f.readlines()
            for l in lines:
                l = l.strip()
                row = 0
                col = 1
                new_line = ''
                for idx, c in enumerate(l):
                    if idx % 9 == 0:
                        row += 1
                        col = 1
                    if c != '.':
                        new_line += '{}{}{} 0\n'.format(row, col, c)
                    col += 1
                yield new_line
