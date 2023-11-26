sayac = 0
for n in range(2,864):
    if(str(2**n)[:3]=="123"):
        sayac += 1
        print(sayac, n,2**n)
