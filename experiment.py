import os
import sys
from tqdm import tqdm
import time

DIR = sys.argv[1]
for root, subdirs, files in os.walk(DIR):
    for f in tqdm(files):
        p = os.path.join(root, f)
        for i in range(1, 5):
            os.system('python3 SAT -S{} -Oresults/{}_damnhard.csv {} &'.format(i, i, p))
        time.sleep(10)
