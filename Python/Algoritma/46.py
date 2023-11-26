m = 2
maksimum = 0 
Collatz = 0
while (m<1000000):
    n = m
    zincir = [n]
    while(n!=1):
        if(n%2==0):
            n = n/2
        else:
            n = 3*n+1
        zincir.append(n)
    if(len(zincir)>maksimum):
        maksimum = len(zincir)
        Collatz = m
    m += 1
print(Collatz)
