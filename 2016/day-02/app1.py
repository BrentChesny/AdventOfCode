buttons = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
i = j = 1
code = ''

for line in open('input.txt').readlines():
	for instruction in line.strip():
		if instruction == 'U' and i > 0:
			i -= 1
		elif instruction == 'D' and i < 2:
			i += 1
		elif instruction == 'L' and j > 0:
			j -= 1
		elif instruction == 'R' and j < 2:
			j += 1

	code += buttons[i][j]

print code
