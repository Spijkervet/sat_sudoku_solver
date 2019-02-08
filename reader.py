import os

class CNF_Reader():
    COMMENT_CHARS = {'p', 'c'}

    def __init__(self):
        self.num_variables = 0
        self.clauses = []


    def read(self, file_name):
        if not os.path.isfile(file_name):
            return None
        with open(file_name, 'r') as file_name:
            lines = file_name.readlines()
            for l in lines:
                l = l.strip()
                if l[0] not in self.COMMENT_CHARS:
                    # Only do something with normal clauses now
                    if l[-1] == '0':
                        cl = [int(l) for l in l.split()[:-1]]
                        self.num_variables = max([abs(l) for l in cl] + [self.num_variables])
                        self.clauses.append(cl)

