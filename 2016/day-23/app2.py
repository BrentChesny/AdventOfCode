instructions = [line.strip().split() for line in open('input2.txt').readlines()]

pointer = 0
registers = {'a': 12, 'b': 0, 'c': 0, 'd': 0} 

def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False

def toggle_instruction(offset):
 	global pointer, instructions

 	if pointer+offset >= len(instructions):
 		return

 	instr = instructions[pointer+offset]

 	if len(instr) == 2:
 		instr[0] = 'dec' if instr[0] == 'inc' else 'inc'
 	elif len(instr) == 3:
 		instr[0] = 'cpy' if instr[0] == 'jnz' else 'jnz'

while pointer < len(instructions):
    parts = instructions[pointer]

    if parts[0] == 'cpy':
    	if not parts[2].isdigit():
        	registers[parts[2]] = int(parts[1]) if is_digit(parts[1]) else registers[parts[1]]
    elif parts[0] == 'inc':
        registers[parts[1]] += 1
    elif parts[0] == 'dec':
        registers[parts[1]] -= 1
    elif parts[0] == 'jnz':
        if parts[1].isdigit() and int(parts[1]) != 0 or registers[parts[1]] != 0:
            pointer += (int(parts[2]) if is_digit(parts[2]) else registers[parts[2]])  - 1
    elif parts[0] == 'tgl':
        offset = int(parts[1]) if is_digit(parts[1]) else registers[parts[1]]
        toggle_instruction(offset)
    elif parts[0] == 'mul':
        x = int(parts[1]) if is_digit(parts[1]) else registers[parts[1]]
        y = int(parts[2]) if is_digit(parts[2]) else registers[parts[2]]
        registers[parts[3]] = x * y
    
    pointer += 1

print registers['a']
