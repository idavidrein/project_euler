def latticePaths(x, y, countX, countY):
	if (x <= 2):
		countX = latticePaths(x + 1, y, countX, countY)
	if (y <= 2):
		countY = latticePaths(x, y + 1, countX, countY)
	if (x == 2 and y == 2):
		return 1
	return countX + countY



num = latticePaths(0, 0, 0, 0)
print (num)