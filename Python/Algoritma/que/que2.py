def number_matrix(r,c):
    matris=[[[] for x in range(0,c)]for x in range(0,r)]
    num=0
    for i in range (0,r):
        num=i+1
        for j in range (0,c):
            matris[i][j]=num
            num+=1
            
    return matris

print("number_matrix(r,c)")
r= int(input("r :"))
c= int(input("c :"))

for i in range (0,len(number_matrix(r,c))):
    for j in range (0,len(number_matrix(r,c)[0])):
        print(number_matrix(r,c)[i][j], end = " ")
    print ()


