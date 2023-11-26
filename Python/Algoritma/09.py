p = int(input("kaçıncı Fibonacci sayısı hesaplansın: "))
fn1, fn2 = 1, 1
for n in range(3, p+1):
    fn3 = fn1 + fn2
    fn1 = fn2
    fn2 = fn3
print(fn3)
