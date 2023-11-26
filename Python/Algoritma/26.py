def isprime(n):
    i = 3
    if(n<2):
        return(0)
    if(n!=2 and n%2==0):
        return(0)
    while(i<=n**(1/2)):
        if(n%i==0):
            return(0)
        i += 2
    return(1)

ikizasallar = []

for n in range(3,101,2):
    if(isprime(n)==1 and isprime(n+2)==1):
        ikizasallar.append([n,n+2])

print(ikizasallar)
