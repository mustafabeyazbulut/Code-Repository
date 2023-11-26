import numpy as np
import collections

myoutputs=range(100)
for i in range(10):
    outcome=np.random.choice(myoutputs)
    print(outcome)
