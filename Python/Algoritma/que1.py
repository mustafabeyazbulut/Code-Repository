def num_digits(num):
    bs = 0
    while(num!=0):
        num = num//10
        bs += 1
    return bs
i=1
while(i!=0):
    print ("Uygulamadan Cikmak icin 0'i tuslayiniz.")
    i= int(input("Bir Sayi Giriniz :"))
    print (num_digits(i))
