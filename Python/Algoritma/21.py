toplam, karetoplam = 0, 0
for n in range(1,101):
    toplam += n
    karetoplam += n**2
print(toplam**2-karetoplam)
