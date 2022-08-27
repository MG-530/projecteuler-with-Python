prime_factors = 600851475143
for num in range(2, prime_factors):
    if prime_factors % num == 0:
        prime_factors = prime_factors / num
        print(num)