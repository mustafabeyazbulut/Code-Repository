def allprimes(n):
    primes = list(range(2,n+1,1))
    for x in range(0,int(n/2)+1):
        if(primes[x]!=0):
            for i in range(x+primes[x],n-1,primes[x]):
                primes[i] = 0
    primes.sort()
    return(primes[primes.count(0):])

a=allprimes(100)





   

