import re

instructions = [(line.split(" ")[0], line.strip().split(" ", 1)[1].split(", ")) for line in open('input.txt')]
registers = {'a' : 1, 'b' : 0}
i = 0

def execute(instruction, args, regs):
	global i

	if instruction == "hlf":
		regs[args[0]] /= 2
	elif instruction == "tpl":
		regs[args[0]] *= 3
	elif instruction == "inc":
		regs[args[0]] += 1
	elif instruction == "jmp":
		i += eval(args[0]) - 1
	elif instruction == "jie" and regs[args[0]] % 2 == 0 or instruction == "jio" and regs[args[0]] == 1:
		i += eval(args[1]) - 1

	i += 1

while i < len(instructions):
	execute(instructions[i][0], instructions[i][1], registers)

print registers