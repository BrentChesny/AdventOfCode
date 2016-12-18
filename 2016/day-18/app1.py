lines = [line.strip() for line in open('input.txt').readlines()]

def next_line(line):
	line = '.' + line + '.'
	new_line = ''

	for i in range(1,len(line)-1):
		left, center, right = line[i-1:i+2]
		if left == center == '^' and right == '.' or left == '.' and center == right == '^' or left == center == '.' and right == '^' or left == '^' and center == right == '.':
			new_line += '^'
		else:
			new_line += '.'

	return new_line

while len(lines) < 40:
	lines.append(next_line(lines[-1]))

print sum(line.count('.') for line in lines)
