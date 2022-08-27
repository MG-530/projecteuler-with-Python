listz = []
for x in range(1000, 1, -1):
    for y in range(1000, 1, -1):
        z = x * y
        zz = str(z)
        bb = zz[::-1]
        if zz == bb:
            listz.append(z)
print(max(listz))
