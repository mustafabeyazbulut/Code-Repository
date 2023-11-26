import numpy as np
import collections


for i in range(10):
    outcome1=np.random.choice([1,2,3,4,5,6])
    outcome2=np.random.choice([1,2,3,4,5,6])
    if outcome1==outcome2:
        print("1. Zar:",outcome1,"  2. Zar:",outcome2," Esittir")
    else:
        print("1. Zar:",outcome1,"  2. Zar:",outcome2," Esit degil")
