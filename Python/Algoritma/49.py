toplam = 0
for i in range(1000,354294):
    kontrol = 0
    for j in str(i):
        kontrol += int(j)**5
    if(i==kontrol):
        toplam += kontrol
print(toplam)
