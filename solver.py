from collections import defaultdict
import random
import numpy as np
import time

class Variable():

    def __init__(self, variable):
        self.variable = variable
        self.assigned = None

    def __repr__(self):
        return 'VAR POINTER: ' + str(self.variable)

class Clause():

    def __init__(self, clause):
        self.clause = clause

    def __repr__(self):
        return '[' + ' '.join([str(c) for c in self.clause]) + ']'

class Clauses():

    def __init__(self, clauses, variables):
        self.clauses = set()
        self.variables = variables
        self.dict = defaultdict(set)
        for c in clauses:
            var_pointer_clause = set()
            for i in c:
                v = self.variables[i]
                var_pointer_clause.add(v)
            clause = Clause(var_pointer_clause) # c
            for v in clause.clause:
                self.dict[v].add(clause)
            self.clauses.add(clause)

    def __repr__(self):
        return ' '.join([str(c) for c in self.clauses])

class Solver():

    def __init__(self, strategy, clauses, variables):
        self.clauses = clauses
        self.variables_min = variables | set(map(lambda x: -1*x, variables))
        self.variables = {v: Variable(v) for v in self.variables_min}
        self.splits = 0
        self.assignments = []
        self.avg_time = 0

    def lookup(self, clauses, variable):
        var_pointer = self.variables[variable.variable]
        return clauses.dict[var_pointer]

    def solve(self):
        # print('Total Clauses: {}'.format(len(clauses.clauses)))
        clauses = Clauses(self.clauses, self.variables)
        solution = self.backtracking(clauses, self.assignments)
        return solution

    def remove_tautologies(self):
        for i, c in enumerate(self.clauses.clauses):
            count = Counter(list(map(abs,c.clause)))
            if 2 in count.values():
                print("TAUTOLOGIE FOUND")
                self.clauses.clauses[i] = []

    def remove_clauses(self, clause_pointers):
        self.clauses.clauses -= clause_pointers

    def remove_occurances(self, clauses, literal):
        for c in clauses:
            c.clause -= set([literal])

    def bcp(self, clauses, unit):
        # remove unit
        modified = set()

        for c in clauses.clauses:
            if unit in c.clause:
                continue
            neg_unit = -1*unit.variable
            neg_var = self.variables[neg_unit]
            if neg_var in c.clause:
                c = Clause([x for x in c.clause if x != neg_var])
                if len(c.clause) == 0:
                    return -1
                modified.add(c)
            else:
                modified.add(c)

        # l = self.lookup(clauses, unit)
        # modified = clauses.clauses - l

        clauses.clauses = modified
        return clauses


    def unit_literal_rule(self, clauses):
        assignment = []
        unit_clauses = [clause for clause in clauses.clauses if len(clause.clause) == 1]
        while len(unit_clauses) > 0:
            literal = list(unit_clauses[0].clause)[0]
            clauses = self.bcp(clauses, literal)
            assignment += [literal]
            if clauses == -1:
                return -1, []
            if not clauses:
                return clauses, assignment

            unit_clauses = [clause for clause in clauses.clauses if len(clause.clause) == 1]
            # self.remove_clauses(l)

            # Delete all occurrences of neg_l from all clauses
            # negative_literal = -1*literal
            # neg_l = self.lookup(negative_literal)
            # self.remove_occurances(neg_l, self.variables[negative_literal])
        return clauses, assignment

    def pure_literal_rule(self, clauses):
        counter = self.get_counter(clauses)
        assignment = []
        pures = []
        for literal, times in counter.items():
            neg_lit = self.variables[-literal.variable]
            if neg_lit not in counter:
                pures.append(literal)

        for pure in pures:
            clauses = self.bcp(clauses, pure)
        assignment += pures
        return clauses, assignment
#         has_pure = False
#         for c in self.clauses.clauses.copy():
#             for var in c.clause:
#                 pos_c = var.variable
#                 neg_c = -1*pos_c
#                 l = self.lookup(neg_c)
#                 self.assignments[pos_c].assigned = True

#                 if len(l) == 0:
#                     delete_pure_literals = self.lookup(pos_c)
#                     self.remove_clauses(delete_pure_literals)
#                     has_pure = True
#         return has_pure

    def get_counter(self, clauses):
        counter = {}
        for clause in clauses.clauses:
            for v in clause.clause:
                if v in counter:
                    counter[v] += 1
                else:
                    counter[v] = 1
        return counter

    def variable_selection(self, clauses):
        counter = self.get_counter(clauses)
        return random.choice(list(counter))


    def backtracking(self, clauses, assignments):
        start_time = time.time()
        # self.remove_tautologies()

        # Unit Literal Rule
        clauses, pure_assignments = self.pure_literal_rule(clauses)
        # print('time', time.time() - start_time)
        clauses, unit_assignments = self.unit_literal_rule(clauses)
        assignments = assignments + pure_assignments + unit_assignments

        if clauses == -1:
            return []
        if not clauses.clauses:
            return assignments

        variable = self.variable_selection(clauses)
        solution = self.backtracking(self.bcp(clauses, variable), assignments + [variable])
        self.splits += 1
        if not solution:
            neg_var = self.variables[-variable.variable]
            solution = self.backtracking(self.bcp(clauses, neg_var), assignments + [neg_var])
        return solution

        # Pure Literal Rule
        # while True:
            # if not self.pure_literal_rule():
                # break
        # self.pure_literal_rule()

        # Empty S Rule
        # if len(self.clauses.clauses) == 0:
            # return True

        # Splitting
        # self.splits += 1
        # add_var = self.variable_selection()

        # solution = self.dpll(clauses + [[add_var]], assignments)
        # if not solution:
            # solution = self.dpll(clauses + [[-add_var]], assignments)
        # if solution:
            # print("SOLUTION FOUND")

