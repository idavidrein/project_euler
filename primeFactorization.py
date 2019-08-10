from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

num = 600851475143
def primeFactorization(n):
	for i in range(2, n):
		if float(n/i).is_integer():
			return primeFactorization(int(n/i))
	return n