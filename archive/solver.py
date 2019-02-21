from collections import defaultdict
import random
import numpy as np


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
        return ' '.join([str(c.variable) for c in self.clause])

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
            clause = Clause(var_pointer_clause)
            for v in var_pointer_clause:
                self.dict[v].add(clause)
            self.clauses.add(clause)

class Solver():

    def __init__(self, strategy, clauses, variables):
        self.variables_min = variables | set(map(lambda x: -1*x, variables))
        self.variables = {v: Variable(v) for v in self.variables_min}
        self.splits = 0

    def lookup(self, variable):
        var_pointer = self.variables[variable]
        return self.clauses.dict[var_pointer]

    def solve(self, clauses, assignments):
        # print('Total Clauses: {}'.format(len(clauses.clauses)))
        assignments = {v: Variable(v) for v in self.variables_min}
        return self.dpll(clauses, assignments)

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

    def unit_literal_rule(self, unit_clauses):
        # Delete all unit clauses containing l
        for clause in unit_clauses:
            literal = list(clause.clause)[0].variable
            l = self.lookup(literal)
            self.remove_clauses(l)

            self.assignments[literal].assigned = True

            # Delete all occurrences of neg_l from all clauses
            negative_literal = -1*literal
            neg_l = self.lookup(negative_literal)
            self.remove_occurances(neg_l, self.variables[negative_literal])

    def pure_literal_rule(self):
        has_pure = False
        for c in self.clauses.clauses.copy():
            for var in c.clause:
                pos_c = var.variable
                neg_c = -1*pos_c
                l = self.lookup(neg_c)
                self.assignments[pos_c].assigned = True

                if len(l) == 0:
                    delete_pure_literals = self.lookup(pos_c)
                    self.remove_clauses(delete_pure_literals)
                    has_pure = True
        return has_pure

    def empty_clause(self):
        for c in self.clauses.clauses:
            if len(c.clause) == 0:
                return True
        return False

    def get_counter(self):
        counter = {}
        for clause in self.clauses.clauses:
            for v in clause.clause:
                if v.variable in counter:
                    counter[v.variable] += 1
                else:
                    counter[v.variable] = 1
        return counter

    def variable_selection(self):
        counter = self.get_counter()
        return random.choice(list(counter))


    def dpll(self, clauses, assignments):
        # self.remove_tautologies()
        self.clauses = Clauses(clauses, self.variables)
        self.assignments = assignments


        # Unit Literal Rule
        # while True:
        unit_clauses = [clause for clause in self.clauses.clauses if len(clause.clause) == 1]
        # if len(unit_clauses) == 0:
            # break
        print(unit_clauses)
        if len(unit_clauses) > 0:
            self.unit_literal_rule(unit_clauses)

        # Pure Literal Rule
        # while True:
            # if not self.pure_literal_rule():
                # break
        # self.pure_literal_rule()

        # Empty Clause Rule
        if self.empty_clause():
            return False

        # Empty S Rule
        if len(self.clauses.clauses) == 0:
            return True

        # Splitting
        self.splits += 1
        add_var = self.variable_selection()

        new_assignments = {k: v for k,v in self.assignments.items()}
        new_assignments[add_var].assigned = True
        new_clauses = []
        for c in self.clauses.clauses:
            new_clauses.append([v.variable for v in c.clause])
        solution = self.dpll(new_clauses + [[add_var]], new_assignments)
        if not solution:
            new_assignments[add_var].assigned = False
            solution = self.dpll(new_clauses + [[-add_var]], new_assignments)
        if solution:
            print("SOLUTION FOUND")
        return solution

