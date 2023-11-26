n = int(input("bir sayı girin: "))
kucuksayi=100
for i in range(0,n):
    sayi = int(input("not giriniz ? "))
    if(kucuksayi>sayi):
        kucuksayi = sayi
print(kucuksayi)
