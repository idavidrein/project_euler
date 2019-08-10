

def collatz(n, init, count):
	if (n == 1):
		return count
	if (n % 2 == 0):
		return collatz(n / 2, init, count + 1)
	else:
		return collatz(3 * n + 1, init, count + 1)


biggest = 0
biggestI = 0
for i in range(1, 1000000):
	if (i % 10000 == 0):
		print(i)
	length = collatz(i, i, 0)
	if (length > biggest):
		biggest = length
		biggestI = i
print(biggestI)
