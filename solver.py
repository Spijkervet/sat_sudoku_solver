import random
import numpy as np
from collections import Counter, defaultdict

class Variable():

    def __init__(self, variable):
        self.variable = variable
        self.flips = 0

    def __repr__(self):
        return 'VAR POINTER: ' + str(self.variable)

class Clause():

    def __init__(self, clause):
        self.clause = clause

class Solver():

    def __init__(self, strategy, clauses, variables):
        self.strategy = strategy
        self.variables_min = variables | set(map(lambda x: -1*x, variables))
        self.variables = {v: Variable(v) for v in self.variables_min}
        self.variables_min = {Variable(v) for v in self.variables_min}


        self.dict = defaultdict(set)
        self.clauses = self.create_clauses(clauses, variables)
        self.splits = 0
        self.backtracks = 0
        self.unit_rule_count = 0
        self.pure_rule_count = 0

        self.assignments = []

        self.counter = Counter()

    def create_clauses(self, clauses, variables):
        new_clauses = set()
        for c in clauses:
            var_pointer_clause = set()
            for i in c:
                v = self.variables[i]
                var_pointer_clause.add(v)
            clause = Clause(var_pointer_clause)
            for v in clause.clause:
                self.dict[v].add(clause)
            new_clauses.add(clause)
        return new_clauses

    def solve(self):
        solution = self.backtracking(self.clauses, self.assignments)
        return solution

    def one_sided_jeroslow_wang(self, clauses):
        counter = Counter()
        for clause in clauses:
            for literal in clause.clause:
                abs_literal = abs(literal.variable)
                abs_var = self.variables[abs_literal]
                counter[abs_var] += 2**-len(clause.clause)
        m = counter.most_common(1)[0]
        return m[0]

    def two_sided_jeroslow_wang(self, clauses):
        counter = Counter()
        for clause in clauses:
            for literal in clause.clause:
                counter[literal] += 2**-len(clause.clause)
        m = counter.most_common(1)[0]
        return m[0]

    def get_counter(self, clauses):
        counter = Counter()
        for clause in clauses:
            for literal in clause.clause:
                counter[literal] += 1
        return counter

    def dlis(self, clauses):
        counter = self.get_counter(clauses)
        return counter.most_common(1)[0][0]

    def rdlis(self, clauses):
        counter = self.get_counter(clauses)
        choices = random.choices(*zip(*counter.items()))
        return choices[0]

    def grab_first(self, clauses, assignments):
        unassigned_vars = self.variables_min - set(assignments)
        # return list(unassigned_vars)[random.choice(range(0,len(unassigned_vars)))]
        return list(unassigned_vars)[0]

    def random_selection(self, clauses, assignments):
        counter = self.get_counter(clauses)
        return random.choice(list(counter))
        # unassigned_vars = self.variables_min - set(assignments)
        # return random.choice(list(unassigned_vars))

    def bcp(self, clauses, unit):
        modified = set()
        for clause in clauses:
            if unit in clause.clause: continue
            neg_unit = self.variables[-unit.variable]
            if neg_unit in clause.clause:
                c = Clause([x for x in clause.clause if x != neg_unit])
                if len(c.clause) == 0: return -1
                modified.add(c)
            else:
                modified.add(clause)
        return modified

    def pure_literal(self, clauses):
        self.pure_rule_count += 1
        counter = self.get_counter(clauses)
        pure_literals = []
        for literal, times in counter.items():
            neg_literal = self.variables[-literal.variable]
            if neg_literal not in counter:
                pure_literals.append(literal)
        for pure in pure_literals:
            clauses = self.bcp(clauses, pure)
        return clauses, pure_literals

    def unit_literal(self, clauses):
        self.unit_rule_count += 1
        unit_literals = []
        unit_clauses = [c.clause for c in clauses if len(c.clause) == 1]
        while len(unit_clauses) > 0:
            unit = list(unit_clauses[0])[0]
            clauses = self.bcp(clauses, unit)
            unit_literals.append(unit)
            if clauses == -1:
                return -1, []
            if not clauses:
                return clauses, unit_literals
            unit_clauses = [c.clause for c in clauses if len(c.clause) == 1]
        return clauses, unit_literals

    def backtracking(self, clauses, assignments):
        clauses, pure_assignment = self.pure_literal(clauses)
        clauses, unit_assignment = self.unit_literal(clauses)
        assignments = assignments + pure_assignment + unit_assignment

        if clauses == -1:
            return []
        if not clauses:
            return assignments

        if self.strategy == 1:
            variable = self.grab_first(clauses, assignments)
        if self.strategy == 2:
            variable = self.dlis(clauses)
        elif self.strategy == 3:
            variable = self.rdlis(clauses)
        elif self.strategy == 4:
            variable = self.one_sided_jeroslow_wang(clauses)
        elif self.strategy == 5:
            variable = self.two_sided_jeroslow_wang(clauses)
        else:
            variable = self.random_selection(clauses, assignments)

        self.splits += 1
        variable.flips += 1
        neg_var = self.variables[-variable.variable]
        solution = self.backtracking(self.bcp(clauses, neg_var), assignments + [neg_var])
        if not solution:
            solution = self.backtracking(self.bcp(clauses, variable), assignments + [variable])
            self.backtracks += 1
        return solution




