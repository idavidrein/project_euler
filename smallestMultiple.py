num = 11152240
divisible = False
while divisible != True:
	if (num % 1000000 == 0):
		print(num)
	if all(num % i == 0 for i in range(1, 21)):
		print(num)
		break
	num += 1
