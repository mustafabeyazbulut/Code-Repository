liste = ["asal", "sayi", "ikiz asal"]
print(liste[1])
print(liste[-1])
liste = [1,2,3,4,5,6,7,8,9,10]
print(liste[2:5])
print(liste[:5])
print(liste[2:])
liste[3] = "pazartesi"
for i in liste:
    print(2*i)
if("pazartesi" in liste):
    print("ok")
len(liste)
liste.__len__()
liste.append(42)
liste.insert(2,42)
liste.remove("pazartesi")
liste.remove(42)

