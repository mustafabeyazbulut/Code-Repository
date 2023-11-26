n = int(input("bir sayı girin: "))

mod=0

if(n//2*2==n):
    binarysayi=""
    while(n>0):
        binarysayi=str(n%2)+binarysayi
        n=n//2
    print("Sayilarin Binary Hali :",binarysayi)
else:
    if(n%2==0 or n%3==0 or n%5==0 or n%7==0):
        print("asal sayı değildir")
    else:
        print("asal sayıdır")
