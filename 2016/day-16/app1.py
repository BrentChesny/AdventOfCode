puzzle_input = '10111011111001111'
disk_size = 272

def cs(value):
    return ''.join(['1' if x == '11' or x == '00' else '0' for x in [value[2*i:2*i+2] for i in range(len(value)/2)]])

def filled_disk(start_state):
    while len(start_state) < disk_size:
        b = ''.join(['1' if c == '0' else '0' for c in start_state[::-1]])

        start_state += '0' + b
    return start_state[:disk_size]

checksum = cs(filled_disk(puzzle_input))
while len(checksum) % 2 == 0:
    checksum = cs(checksum)

print checksum