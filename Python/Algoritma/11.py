p = int(input("bir sayı girin: "))
for n in range(2, p//2+1):
    if(p//n*n==p):
        print(n)
