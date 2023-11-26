p = int(input("hangi sayıya kadar olan asal sayılar hesaplansın: "))
n = 2
asal = []
while(n<p):
    i = 3
    asalmi = 1
    if(n!=2 and n%2==0):
        asalmi = 0
    else:
        while(i<=n**(1/2)):
            if(n%i==0):
                asalmi = 0
            i += 2
    if(asalmi == 1):
        asal.append(n)
    n += 1
print(asal)
