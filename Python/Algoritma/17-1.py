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

n = int(input("bir sayı girin: "))
if(isprime(n)==1):
    print("asal sayıdır")
else:
    print("asal sayı değildir")
        
