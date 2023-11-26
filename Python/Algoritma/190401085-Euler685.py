import math
sayac = 0
toplam=1
sayi = 678910

# ilk sayıyı bulmak için
for n in range(0,100):
    if(str(2**n)[:3]=="123"):
            sayac += 1
            break
# ilk sayıyı bulmak için

p90=int(str(2**90)[:15])
p196=int(str(2**196)[:15])
p289=int(str(2**289)[:15])
p485=int(str(2**485)[:15])
toplam=int(str(toplam*p90)[:15])
       

# ilk üç rakamı 123 olan 2 nin katsayıları arasında 196,289,485
# olarak bir artış vardır.
while(sayac!=sayi):
    if(str(toplam*p196)[:3]=="123"):
       sayac +=1
       toplam=int(str(toplam*p196)[:15])
       n+=196
    elif(str(toplam*p289)[:3]=="123"):
       sayac +=1
       toplam=int(str(toplam*p289)[:15])
       n+=289
    elif(str(toplam*p485)[:3]=="123"):
       sayac +=1
       toplam=int(str(toplam*p485)[:15])
       n+=485
print (sayac,n, toplam) 
