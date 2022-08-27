#finding multiplier
sum = 0
for x in range(1000):
    if x % 5 == 0:
        sum += x
        # print(x)
    elif x % 3 == 0:
        # print(x)
        sum += x
    elif x % 15 == 0:
        sum -= x
print(sum)
