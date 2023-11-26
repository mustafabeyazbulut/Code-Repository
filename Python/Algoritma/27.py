def isprime(n):
    i = 3
    if(n<2):
        return(0)
    if(n!=2 and n%2==0):
        return(0)
    while(i<=n**(1/2)):
        if(n%i==0):
            return(0)
        i += 2
    return(1)

fn1, fn2 = 1, 1
fn3 = 42
toplam = 0

while(fn3<10000):
    fn3 = fn1 + fn2
    if(isprime(fn3)==1):
        toplam += fn3
    fn1,fn2 = fn2,fn3

print(toplam)
