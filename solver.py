from collections import defaultdict, Counter

class Clauses():

    def __init__(self, clauses):
        self.list = clauses
        self.dict = defaultdict(list)
        counter = 0
        for c in clauses:
            for i in c:
                self.dict[i].append(counter)
            counter += 1

class Solver():

    def __init__(self, strategy, clauses, variables):
        self.clauses = Clauses(clauses)
        self.variables = variables

    def lookup(self, literal):
        return self.clauses.dict[literal]

    def solve(self):
        # print(clauses)
        print('Total Clauses: {}'.format(len(self.clauses.list)))
        return self.dpll()

    def remove_tautologies(self):
        for i, c in enumerate(self.clauses.list):
            count = Counter(list(map(abs,c)))
            if 2 in count.values():
                print("TAUTOLOGIE FOUND")
                self.clauses.list[i] = []

    def remove_clause(self, clause_num):
        print("REMOVED", self.clauses.list[clause_num])
        self.clauses.list[clause_num] = []

    def remove_occurance(self, clause_num, literal):
        print("REMOVING", literal, "FROM", self.clauses.list[clause_num])
        self.clauses.list[clause_num].remove(literal)

    def unit_literal_rule(self, literal):
        # Delete all unit clauses containing l
        lookup = self.lookup(literal)
        for l in lookup:
            self.remove_clause(l)

        # Delete all occurrences of neg_l from all clauses
        neg_literal = -1*literal
        lookup = self.lookup(neg_literal)
        for l in lookup:
            self.remove_occurance(l, neg_literal)

    def pure_literal_rule(self, clause):
        for c in clause:
            neg_c = -1*c
            l = self.lookup(neg_c)
            if len(l) == 0:
                print("PURE LITERAL", l)
                delete_pure_literals = self.lookup(c)
                for l in delete_pure_literals:
                    self.remove_clause(l)


    def dpll(self):
        self.remove_tautologies()
        #  DPLL:
        # Run BCP on the formula.
        # If the formula evaluates to True, return True.
        # If the formula evaluates to False, return False.
        # If the formula is still Undecided:
        # Choose the next unassigned variable.
        # Return (DPLL with that variable True) || (DPLL with that variable False)
        for i in self.clauses.list:
            if len(i) == 1:
                l = i[0]
                self.unit_literal_rule(l)
            self.pure_literal_rule(i)


    def unit_propagation(self):
        pass
