fn1, fn2, fn3, toplam = 1, 1, 0, 0
while(fn3<4000000):
    if(fn3%2==0):
        toplam += fn3
    fn3 = fn1 + fn2
    fn1, fn2 = fn2, fn3
print(toplam)
