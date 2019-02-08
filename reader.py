import os

class CNF_Reader():
    COMMENT_CHARS = {'p', 'c'}

    def __init__(self):
        self.num_variables = 0
        self.clauses = []

    def read_string(self, lines):
        lines = lines.split('\n')
        for l in lines:
            l = l.strip()
            if len(l) > 0 and l[0] not in self.COMMENT_CHARS:
                # Only do something with normal clauses now
                if l[-1] == '0':
                    cl = [int(l) for l in l.split()[:-1]]
                    self.num_variables = max([abs(l) for l in cl] + [self.num_variables])
                    self.clauses.append(cl)


    def read(self, file_name):
        assert os.path.isfile(file_name), "Sudoku CNF rules file does not exist"
        with open(file_name, 'r') as file_name:
            self.read_string(file_name.read())
