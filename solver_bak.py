import random

class Solver():

    def __init__(self, strategy, clauses, variables):
        self.strategy = strategy
        self.clauses = clauses
        self.variables = variables
        self.splits = 0
        self.assignments = []

    def solve(self):
        solution = self.backtracking(self.clauses, self.assignments)
        return solution

    def get_counter(self, clauses):
        counter = {}
        for clause in clauses:
            for literal in clause:
                if literal in counter:
                    counter[literal] += 1
                else:
                    counter[literal] = 1
        return counter

    def variable_selection(self, clauses):
        counter = self.get_counter(clauses)
        return random.choice(list(counter))

    def bcp(self, clauses, unit):
        modified = []
        for clause in clauses:
            if unit in clause: continue
            if -unit in clause:
                c = [x for x in clause if x != -unit]
                if len(c) == 0: return -1
                modified.append(c)
            else:
                modified.append(clause)
        return modified

    def pure_literal(self, clauses):
        counter = self.get_counter(clauses)
        assignment = []
        pures = []
        for literal, times in counter.items():
            if -literal not in counter:
                pures.append(literal)
        for pure in pures:
            clauses = self.bcp(clauses, pure)
        assignment += pures
        return clauses, assignment

    def unit_literal(self, clauses):
        assignment = []
        unit_clauses = [c for c in clauses if len(c) == 1]
        while len(unit_clauses) > 0:
            unit = unit_clauses[0]
            clauses = self.bcp(clauses, unit[0])
            assignment += [unit[0]]
            if clauses == -1:
                return -1, []
            if not clauses:
                return clauses, assignment
            unit_clauses = [c for c in clauses if len(c) == 1]
        return clauses, assignment

    def backtracking(self, clauses, assignments):
        clauses, pure_assignment = self.pure_literal(clauses)
        clauses, unit_assignment = self.unit_literal(clauses)
        assignments = assignments + pure_assignment + unit_assignment

        if clauses == -1:
            return []
        if not clauses:
            return assignments

        variable = self.variable_selection(clauses)
        solution = self.backtracking(self.bcp(clauses, variable), assignments + [variable])
        if not solution:
            solution = self.backtracking(self.bcp(clauses, -variable), assignments + [-variable])
        return solution




