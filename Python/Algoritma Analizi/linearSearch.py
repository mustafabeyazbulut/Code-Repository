

def linearSearch(list_1,item):
    found=False
    s=0
    n=len(list_1)
    for i in range(n):
        s+=1
        if list_1[i]==item:
            found=True
            break
    return found,s

testlist=[0,1,2,8,13,17,19,32,42,50]

print(linearSearch(testlist,3))
print(linearSearch(testlist,0))

