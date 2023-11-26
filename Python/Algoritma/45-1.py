from fonksiyon import divisors

ucgen,i = 1, 2

while(len(divisors(ucgen))<500):
    ucgen += i
    i += 1

print(ucgen)
