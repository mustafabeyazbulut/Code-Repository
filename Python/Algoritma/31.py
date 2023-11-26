m = int(input("sayı: "))
for n in range(1,10,2):
    for p in range(2,m,2):
        if p**2<n:
            print(p)
