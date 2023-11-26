p = int(input("bir sayı girin: "))
bolenler = []
for n in range(2, p//2+1):
    if(p//n*n==p):
        bolenler.append(n)
print(bolenler)
