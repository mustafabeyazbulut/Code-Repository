a=input("istediğiniz kadar rakam: ")
lst=a.split()
z =len(lst)

toplam=0
a = []
for i in range(z):
    k=int(lst[i])
    toplam +=k
    a.append(k)

ort= toplam/z
print("Liste İçindeki En Büyük Sayı :", max(a), "\nListe İçindeki En Küçük Sayı :", min(a),"Ortalama:",ort)
