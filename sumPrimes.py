from primeFactorization import isPrime

total = 0
for i in range(1, 2000000):
	if isPrime(i):
		total += i
	if i % 200000 == 0:
		print(i)
print(total)