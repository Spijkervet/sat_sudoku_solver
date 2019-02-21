class Test():

    def __init__(self):
        pass



c = Test()
c2 = Test()

l = set()
l.add(c)
l.add(c2)

print("C1", c, "C2", c2)
print(l)
l -= set([c])

print(l)
