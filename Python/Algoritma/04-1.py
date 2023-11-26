a = int(input("x karenin katsayısını girin: "))
b = int(input("x in katsayısını girin: "))
c = int(input("sabit terimi girin: "))

def delta(a, b, c):
    return(b**2-4*a*c)

if(delta(a,b,c)>0):
    x1 = (-b+delta(a,b,c)**(1/2))/(2*a)
    x2 = (-b-delta(a,b,c)**(1/2))/(2*a)
    print(x1, x2)
elif(delta(a,b,c)==0):
    x1 = -b/(2*a)
    print(x1)
else:
    print("Reel kök yoktur")
