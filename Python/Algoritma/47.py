kuvvet = set()
for a in range(2,101):
    for b in range(2,101):
        kuvvet.add(a**b)
print(len(kuvvet))
