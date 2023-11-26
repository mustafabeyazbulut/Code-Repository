dosya=open("p067_triangle.txt")
ucgen = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    ucgen.append(line)
dosya.close()

for n in range(len(ucgen)-2,-1,-1):
    for m in range(len(ucgen[n])):
        ucgen[n][m] = int(ucgen[n][m]) +  max(int(ucgen[n+1][m]),int(ucgen[n+1][m+1]))

print(ucgen[0][0])
