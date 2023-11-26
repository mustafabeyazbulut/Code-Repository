from fonksiyon import divisors

liste = []
toplamlar = set()

for n in range(11,28123):
    if(sum(divisors(n))>n):
        liste.append(n)

for p in liste:
    for q in liste:
        if(p+q<28123):
            toplamlar.add(p+q)

sayilar = set(range(1,28123))

print(sum(sayilar-toplamlar))
