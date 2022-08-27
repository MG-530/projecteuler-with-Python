list=[2]
def isprime(num):
    if num % 2 == 0:
        return False
    else:

        for n in range(3, int(num ** 0.5) + 1, 2):
            if num % n == 0:
                return False
        return list.append(num)


for num in range(2, 1000000):
    isprime(num)
print(list[10000])
