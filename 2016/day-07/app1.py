import re

def is_abba(abba):
	return abba[3] == abba[0] != abba[1] == abba[2]

def has_abba(line):
	for i in range(len(line)-3):
		if is_abba(line[i:i+4]):
			return True

	return False

def valid(line):
	line = line.replace('[', '(')
	line = line.replace(']', ')')

	brackets = re.findall(r'\([^()]*\)', line)
	line = re.sub(r'\([^()]*\)', '-', line)

	if has_abba(line) and not any(has_abba(part) for part in brackets):
		return True

	return False

print sum(1 for line in open('input.txt').readlines() if valid(line.strip()))