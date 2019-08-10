total = 0
prev = 1
current = 0
while current < 4000000:
	tmp = current
	current += prev
	prev = tmp
	if current % 2 == 0:
		total += current
print(current)
