import random
sayi = random.randint(1,100)
tahmin,deneme = 0, 0
while(tahmin!=sayi):
    tahmin = int(input("tahmininiz nedir: "))
    deneme += 1
    if(tahmin>sayi):
        print("daha büyük bir tahminde bulundunuz")
    elif(tahmin<sayi):
        print("daha küçük bir tahminde bulundunuz")
print("bildiniz",deneme)
