n = int(input("bir sayı girin: "))
pi,kesir=0,0
# girilen n sayısına göre
tek= (2*n)+1 
i= (2*n)+1
# kesirin son rakamında 9+ 2n+1 n=4
# kısmını bulmak için gerekli kod.
# bu pi nin kendi özelliğinde yer alıyor

# bu kod kesirin 9+ rakamından geriye
# doğru döngü oluşturan kod.
# 9 burada 2n+1 n=4 olarak düşünmelisiniz
# 2 şer 2 şer azalıyor 1 e kadar
while (i>0):
   kesir+=1
   i-=2
# bu kod sonucunda örnek olarak
# 9 7 5 3 1 yan tarafında yer alan
# kesirdeki son rakam bulunur
# örnek olarak 1 yanındaki 1
# 3 ün yanında ki 2
# son olarak sonuncu sayının yanındaki
# kesirin üstünde yer alan sayı
# 9 u örnek alırsak 9 un yanında bulunan
# 5^2 yi kesir değişkenine atamasını yapar

pi=(kesir*kesir)+tek # kesrin son kısmında yer alan 9 + 5^2 hesaplar

# bu kod kesir sayısı 1 olana kadar döner
# bu esnada kesrin son işleminden başlar
# 9+ 5^2 den başlar. Bu değeri pi ye atar
# sonra kesrin alt kısmı pi değişkeni olur
while (tek>1):
    tek-=2
    kesir-=1
    pi=(((pi*tek)+(kesir*kesir))/pi)
# pi değişkenini alır ve örnek olarak
# 7 + (4^2) / pi işlemini
# ((pi*7)+ (4^2)) /pi yi hesaplar
# kesrin son rakamı 1 olana kadar döner



pi=4/pi # bu kod kesrin en üstündeki 4 e pi yi böler

print (pi)
