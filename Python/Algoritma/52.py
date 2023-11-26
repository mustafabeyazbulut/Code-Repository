from fonksiyon import allprimes
from fonksiyon import isprime

asal = allprimes(4000)

for p in range(5,len(asal)):
    for a in range(0,len(asal)-p):
        if(isprime(sum(asal[a:a+p]))==1 and sum(asal[a:a+p])<1000000):
            toplam = sum(asal[a:a+p])

print(toplam)
