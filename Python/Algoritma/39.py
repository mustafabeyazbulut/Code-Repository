alt, ust = 1, 100
sonuc = 42
while(sonuc!=0):
    tahmin = (alt+ust)//2
    print(tahmin)
    sonuc = int(input("tahiminin durumu nedir: "))
    if(sonuc = 1):
        ust = tahmin
    elif(sonuc = -1):
        alt = tahmin
print("oyun bitti")
