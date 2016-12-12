instructions = [line.strip() for line in open('input.txt').readlines()]

pointer = 0
registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}  

while pointer < len(instructions):
    parts = instructions[pointer].split()

    if parts[0] == 'cpy':
        registers[parts[2]] = int(parts[1]) if parts[1].isdigit() else registers[parts[1]]
    elif parts[0] == 'inc':
        registers[parts[1]] += 1
    elif parts[0] == 'dec':
        registers[parts[1]] -= 1
    elif parts[0] == 'jnz':
        if parts[1].isdigit() and int(parts[1]) != 0 or registers[parts[1]] != 0:
            pointer += int(parts[2]) - 1

    pointer += 1

print registers['a']
