n = int(input("bir sayı girin: "))
bt = 0
i=0
j=0
k=0
bt = n - (n//10)*10
n = n//10
while(n!=0):
    if(bt>=n - (n//10)*10):
        i+=1
    if(bt<=n - (n//10)*10):
        j+=1
    k+=1
    bt = n - (n//10)*10
    n = n//10
    


if(k==i): print("sayisi Artan Sayidir.")
elif (k==j):print("sayisi Azalan Sayidir.")
else: print("sayisi dalgali sayidir.")
