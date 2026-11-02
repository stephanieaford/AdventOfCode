file = open("dayoneinput.txt").read()
rotations = file.splitlines()
position = 50
zero_count_p1 = 0
zero_count_p2 = 0

for line in rotations:
	direction = line[0]
	amount = int(line[1:])

	for _ in range(amount):
		if direction=='L':
			position = (position - 1 + 100) % 100
		else:
			position = (position + 1) % 100
		if position == 0:
			zero_count_p2 += 1
	if position == 0:
		zero_count_p1 += 1

print(zero_count_p1)
print(zero_count_p2)
