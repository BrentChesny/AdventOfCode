instructions = [line.strip().split() for line in open('input.txt').readlines()]

def interpret(a, instructions):
	pointer = 0
	registers = {'a': a, 'b': 0, 'c': 0, 'd': 0}
	last_out = 1

	while pointer < len(instructions):
	    parts = instructions[pointer]

	    if parts[0] == 'cpy':
	    	if not parts[2].isdigit():
	        	registers[parts[2]] = registers[parts[1]] if parts[1] in registers else int(parts[1])
	    elif parts[0] == 'inc':
	        registers[parts[1]] += 1
	    elif parts[0] == 'dec':
	        registers[parts[1]] -= 1
	    elif parts[0] == 'jnz':
	        if parts[1].isdigit() and int(parts[1]) != 0 or parts[1] in registers and registers[parts[1]] != 0:
	            pointer += (registers[parts[2]] if parts[2] in registers else int(parts[2]))  - 1
	    elif parts[0] == 'out':
	    	out = registers[parts[1]] if parts[1] in registers else int(parts[1])
	    	if out == last_out:
	    		print 'Not: ', a
	    		return
	    	else:
	    		last_out = out
	    pointer += 1

for a in xrange(10000):
	interpret(a, instructions)
