import numpy as np
import collections

my_outputs=np.zeros((100),dtype=int)
my_outputs[0]=1

for i in range(20000):
    outcome=np.random.choice(my_outputs)
    if outcome==1:
        print (i," th is positive ")
        break
