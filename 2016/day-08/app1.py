import re

screen = [['.' for i in range(50)] for j in range(6)]

def parse_instruction(instruction):
	parts = re.split(r'(\d+)', instruction)
	return (parts[0], int(parts[1]), int(parts[3]))

def do_op(screen, op, arg1, arg2):
	if op == 'rect ':
		for i in range(arg2):
			for j in range(arg1):
				screen[i][j] = '#'
	elif op == 'rotate row y=':
		for i in range(arg2):
			screen[arg1] = [screen[arg1][-1]] + screen[arg1][:-1]
	elif op == 'rotate column x=':
		screen = map(list, zip(*screen))
		screen = do_op(screen, 'rotate row y=', arg1, arg2)
		screen = map(list, zip(*screen))

	return screen

for instruction in map(parse_instruction, open('input.txt').readlines()):
	screen = do_op(screen, *instruction)

print sum([sum([1 for i in line if i == '#']) for line in screen])