def ispalindrome(n):
    if(str(n)==str(n)[::-1]):
        return(1)
    else:
        return(0)

lychrel = 0

for m in range(1,10000):
    n = m
    for i in range(50):
        if(ispalindrome(n+int(str(n)[::-1]))==1):
            break
        else:
            n += int(str(n)[::-1])
    else:
        lychrel += 1
print(lychrel)
