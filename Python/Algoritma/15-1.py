euler, p, faktoriyel = 2, 2, 1
while(p<10):
    faktoriyel = faktoriyel * p
    euler = euler + 1/faktoriyel
    p += 1
print(euler)
