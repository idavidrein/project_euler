from primeFactorization import isPrime

count = 0
i = 0
while (True):
	if count == 10001:
		break
	if isPrime(i):
		if count >= 9999:
			print(i)
		count += 1
	i += 1
print(i)
print(isPrime(13))
print(isPrime(29))
print(isPrime(44))
print(isPrime(104743))
