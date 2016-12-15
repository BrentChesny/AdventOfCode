import re

discs = [map(int, re.match('Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+)', line).groups()) for line in open('input_2.txt').readlines()]

time = 0

while True:
    time_found = True

    for nr, size, pos in discs:
        current_time = time + nr
        current_pos = (pos + current_time) % size

        if current_pos != 0:
            time_found = False
            break

    if time_found:
        break

    time += 1

print time