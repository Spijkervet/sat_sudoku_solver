import os
from src.converter import Sudoku_CNF
from src.reader import CNF_Reader


SUDOKU_PATH = 'test_data'
OUTPUT_PATH = 'test_data/cnf/sudoku'


sudoku_rules = open('./test_data/cnf/sudoku-rules.cnf', 'r').read()

for root, subdirs, files in os.walk(SUDOKU_PATH):
    for f in files:
        p = os.path.join(root, f)
        sud_conv = Sudoku_CNF()
        print(p)
        conv = sud_conv.convert(p)
        for idx, (c, size) in enumerate(conv):
            write_path = os.path.join(OUTPUT_PATH, f)
            if not os.path.exists(write_path):
                os.mkdir(write_path)

            handle = open(os.path.join(write_path, str(idx) + '.txt'), 'w')
            appended = sudoku_rules + c
            handle.write(appended)
            handle.close()


