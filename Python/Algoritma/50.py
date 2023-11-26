from math import factorial
sonuc = 0
for n in range(3,100000):
    toplam = 0
    for i in str(n):
        toplam += factorial(int(i))
    if(n==toplam):
        sonuc += n
        print(n)
print(sonuc)
