from collections import deque

instructions = [line.split() for line in open('input.txt').readlines()]
password = 'fbgdceah'

def rotate_based_on(password, based_on):
	x = based_on
	i = password.index(x)
	m = i + 1 + (i >= 4)
	password = deque(password)
	password.rotate(m)
	return list(password)

def revert_rotate_based_on(password, based_on):
	pw = password[:]
	while password != rotate_based_on(pw, based_on):
		pw = pw[1:] + pw[:1]
	return pw

def undo_instruction(password, instruction):
	password = list(password)

	if instruction[0] == 'swap' and instruction[1] == 'position':
		x = int(instruction[2])
		y = int(instruction[5])
		password[x], password[y] = password[y], password[x]
	elif instruction[0] == 'swap' and instruction[1] == 'letter':
		password = ''.join(password)
		password = password.replace(instruction[2], '-')
		password = password.replace(instruction[5], instruction[2])
		password = password.replace('-', instruction[5])
		password = list(password)
	elif instruction[0] == 'rotate' and instruction[1] == 'left' or instruction[1] == 'right':
		arg = int(instruction[2])
		arg *= 1 if instruction[1] == 'left' else -1
		password = deque(password)
		password.rotate(arg)
		password = list(password)
	elif instruction[0] == 'rotate' and instruction[1] == 'based':
		password = revert_rotate_based_on(password, instruction[6])
	elif instruction[0] == 'reverse':
		x = int(instruction[2])
		y = int(instruction[4])
		a, b, c = password[:x], password[x:y+1], password[y+1:]
		password = a + b[::-1] + c
	elif instruction[0] == 'move':
		x = int(instruction[2])
		y = int(instruction[5])
		c = password.pop(y)
		password.insert(x, c)

	return ''.join(password)

for instruction in instructions[::-1]:
	password = undo_instruction(password, instruction)

print password