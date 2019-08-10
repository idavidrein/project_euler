count = 0
for b in range(0, 1001):
	for a in range(0, 1001):
		count += 1
		c = a**2 + b**2
		c = c**(1/2.0)
		if (a + b + c) == 1000:
			print(a*b*c)
print(count)