import numpy as np
import collections

t=[]
for i in range(10):
    t.append(np.random.choice(['H','T']))
print(t)
print(collections.Counter(t))

