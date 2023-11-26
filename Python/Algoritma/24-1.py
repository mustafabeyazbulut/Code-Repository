n = int(input("hangi sayıya kadar olan asal sayılar hesaplansın: "))
primes=list(range(2,n+1,1))
for x in range(0,int(n/2)+1):
    if(primes[x]!=0):
        for i in range(x+primes[x],n-1,primes[x]):
            primes[i] = 0
primes.sort()
print(primes[primes.count(0):])
