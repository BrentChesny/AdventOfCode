import re

ranges = sorted([tuple(map(int, re.match('(\d+)-(\d+)', line).groups())) for line in open('input.txt').readlines()])
count = 0

current_begin, current_end = ranges[0]
for begin, end in ranges[1:]:
	if begin <= current_end + 1:
		current_begin = begin
		current_end = max(current_end, end)
	else:
		count += begin - current_end - 1 
		current_begin, current_end = begin, end

print 'Number of non-blocked IPs:', count

