#hem kendisi hemde ters yazılışı birer asal sayı olan
#1 milyondan küçük kaç emirp sayısı vardır.

def allprimes(n):
    primes = list(range(2,n+1,1))
    for x in range(0,int(n/2)+1):
        if(primes[x]!=0):
            for i in range(x+primes[x],n-1,primes[x]):
                primes[i] = 0
    primes.sort()
    return(primes[primes.count(0):])

a=allprimes(1000000)
emirp=[]
for i in range(0,len(a)):
   sayi = a[i]
   ters = 0
   
   while( sayi > 0):
       gecici = sayi %10
       ters = (ters *10) + gecici
       sayi = sayi //10

   if(ters>11):
       if(ters in a):
           emirp.append(ters)
print(len(emirp))
