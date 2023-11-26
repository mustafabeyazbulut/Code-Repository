import numpy as np
import collections

my_outputs=np.zeros((100),dtype=int)
my_outputs[0]=1

for i in range(20):
    print(np.random.choice(my_outputs))
