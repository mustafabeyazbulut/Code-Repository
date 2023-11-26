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

n,p = 0, 1

while(n<10001):
    p += 1
    if(isprime(p)==1):
        n += 1

print(p)
