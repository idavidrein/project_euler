sumSquares = 0
squareSum = 0
for i in range(1, 101):
	sumSquares += i**2
for i in range(1, 101):
	squareSum += i
squareSum = squareSum**2
print(squareSum - sumSquares)