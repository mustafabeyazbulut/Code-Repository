import numpy as np
import collections

def my_exp(x):
    for i in range(x):
        t=[]
        for i in range(10):
            t.append(np.random.choice(['H','T']))
        print(collections.Counter(t))

my_exp(5)
