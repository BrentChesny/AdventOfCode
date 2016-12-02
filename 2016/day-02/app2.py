buttons = [[None, None, '1', None, None], [None, '2', '3', '4', None], ['5', '6', '7', '8', '9'], [None, 'A', 'B', 'C', None], [None, None, 'D', None, None]]
i = 2
j = 0
code = ''

for line in open('input.txt').readlines():
	for instruction in line.strip():
		if instruction == 'U' and i > 0 and buttons[i-1][j] != None:
			i -= 1
		elif instruction == 'D' and i < 4 and buttons[i+1][j] != None:
			i += 1
		elif instruction == 'L' and j > 0 and buttons[i][j-1] != None:
			j -= 1
		elif instruction == 'R' and j < 4 and buttons[i][j+1] != None:
			j += 1

	code += buttons[i][j]

print code
