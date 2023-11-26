import math

i= 90
rank = 0
previ=0
lowerbound = math.log(1.23,10)
upperbound = math.log(1.24,10)

def testdf(i):
    logi = math.log(2,10)*i
    diff = (logi - int(logi))    
    return diff

while(rank<379):
    diff = testdf(i)
    if (diff)>=upperbound:
        i+=93
    elif(diff < lowerbound):
        i+=196
    else:
        rank+=1
        previ=i
        i+=196
    print(diff)
print(diff,rank,previ)
