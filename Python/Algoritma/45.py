ucgen,i = 1, 2
bs = 2
while(bs<500):
    ucgen = ucgen + i
    bs = 2
    for n in range(2, ucgen//2+1):
        if(ucgen//n*n==ucgen):
            bs += 1
    i += 1
print(ucgen)
