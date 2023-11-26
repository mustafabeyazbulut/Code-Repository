n = int(input("bir sayı girin: "))
pi=0
n= (2*n)+1
pi=(n*n)+2
while (n!=1):
    pi = ((pi*2)+(n*n))/pi
    n -=2
pi = ((pi*1)+(n*n))/pi
pi =4/pi
print (pi)
