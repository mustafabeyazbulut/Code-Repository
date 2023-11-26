import random
liste=[]

for i in range(26,1,-1):
    for b in range(0,random.randint(1,10)):
        liste.append(0)
    toplam = 1
    for n in range(2, i // 2 + 1):
        if (i // n * n == i):
            toplam += n
    liste.append(toplam)
print(liste)
