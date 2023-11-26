from fonksiyon import isprime
fn1, fn2 = 1, 1
fn3 = 42
toplam = 0

while(fn3<10000):
    fn3 = fn1 + fn2
    if(isprime(fn3)==1):
        toplam += fn3
    fn1,fn2 = fn2,fn3

print(toplam)
