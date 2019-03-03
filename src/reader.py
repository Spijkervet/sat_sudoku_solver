import os

class CNF_Reader():
    COMMENT_CHARS = {'p', 'c'}

    def __init__(self, size):
        self.num_variables = 0
        self.variables = set()
        self.givens = 0
        self.clauses = []
        self.size = size

    def bound_check(self, l):
        return True
        # l = l.replace('-', '')
        # if int(l[0]) > self.size:
        #     return False
        # if int(l[1]) > self.size:
        #     return False
        # return True

    def read_string(self, lines):
        lines = lines.split('\n')
        # 11989 number of clauses for Sudoku rules, minus one \n
        self.givens = len(lines[11989:]) - 1
        for l in lines:
            l = l.strip()
            # print(l, self.size)
            if len(l) > 0 and l[0] not in self.COMMENT_CHARS:
                # Only do something with normal clauses now
                if l[-1] == '0':
                    cl = [int(l) for l in l.split()[:-1]]
                    self.variables.update([abs(l) for l in cl])
                    self.clauses.append(cl)



    def read(self, file_name):
        with open(file_name, 'r') as f:
            self.read_string(f.read())
