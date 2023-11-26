def d(p):
    toplam = 1
    q = int(p**(1/2)//1)+1
    for n in range(2, q):
        if(p//n*n==p):
            toplam += n + p/n
    return(toplam)

gtoplam = 0

for m in range(2,10000):
    s = d(m)
    if(m==s):
        continue
    if(s>10000):
        continue
    if(m==d(s)):
        gtoplam += m

print(gtoplam)
