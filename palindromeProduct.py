big = 0
for i in range(999, 100, -1):
	for j in range(999, 100, -1):
		string = str(i*j)
		stringR = string[::-1]
		if (string == stringR):
			if i*j > big:
				big = i*j
print(big)