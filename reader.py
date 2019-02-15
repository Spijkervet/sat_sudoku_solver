import os

class CNF_Reader():
    COMMENT_CHARS = {'p', 'c'}

    def __init__(self):
        self.num_variables = 0
        self.variables = set()
        self.clauses = []
        self.old_clauses = []

    def read_string(self, lines):
        lines = lines.split('\n')
        for l in lines:
            l = l.strip()
            if len(l) > 0 and l[0] not in self.COMMENT_CHARS:
                # Only do something with normal clauses now
                if l[-1] == '0':
                    cl = [int(l) for l in l.split()[:-1]]
                    cl2 = [(abs(int(l)), True) if int(l) > 0 else (abs(int(l)), False) for l in l.split()[:-1]]
                    self.num_variables = max([abs(l) for l in cl] + [self.num_variables])
                    self.variables.update([abs(l) for l in cl])
                    self.old_clauses.append(cl)
                    self.clauses.append(cl) #cl2



    def read(self, file_name):
        assert os.path.isfile(file_name), "Sudoku CNF rules file does not exist"
        with open(file_name, 'r') as file_name:
            self.read_string(file_name.read())
