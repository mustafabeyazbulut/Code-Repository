sayac, i , n = 0, 1, 0
while (sayac < 678910):
    i = int(str(i * 2)[:15])
    n += 1
    if (str(i)[:3] == '123'):
        sayac += 1
print(n)

