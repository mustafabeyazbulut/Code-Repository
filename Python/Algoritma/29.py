bolenler = [1, 1]
for p in range(2,10**7):
    bs = 2
    for n in range(2, p//2+1):
        if(p//n*n==p):
            bs += 1
    bolenler.append(bs)
    print(p)
print(bolenler)
