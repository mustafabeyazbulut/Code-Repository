b=0;
j=0;
i=0


while(j!=689):
    i+=1
    b=i
    while(b!=0):
        if( (b - (b//10)*10)==1):
            j+=1
        b = b//10

print (i)



    
