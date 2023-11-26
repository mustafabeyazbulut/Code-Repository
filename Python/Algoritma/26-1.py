from fonksiyon import isprime

ikizasallar = []

for n in range(3,101,2):
    if(isprime(n)==1 and isprime(n+2)==1):
        ikizasallar.append([n,n+2])

print(ikizasallar)
