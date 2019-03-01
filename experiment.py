import os
import sys

DIR = sys.argv[1]
for root, subdirs, files in os.walk(DIR):
    for f in files:
        p = os.path.join(root, f)
        print("RUNNING", p)
        os.system('python3.6 SAT -S2 ' + p)
