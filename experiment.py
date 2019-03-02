import os
import sys
from tqdm import tqdm

DIR = sys.argv[1]
for root, subdirs, files in os.walk(DIR):
    for f in tqdm(files):
        p = os.path.join(root, f)
        os.system('python3 SAT -S2 -Oresults_grab_first_1000.csv ' + p)
