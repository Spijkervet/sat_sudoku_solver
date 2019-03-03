import os
import sys
from tqdm import tqdm
import time

DIR = sys.argv[1]
for root, subdirs, files in os.walk(DIR):
    for f in tqdm(files):
        p = os.path.join(root, f)
        for i in range(2,3):
            os.system('python3 SAT -S{} -Oresults/{}_1000.csv {}'.format(i, i, p))
