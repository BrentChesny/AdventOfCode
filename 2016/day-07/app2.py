import re

def is_aba(aba):
	return aba[2] == aba[0] != aba[1]

def get_abas(line):
	abas = set()

	for i in range(len(line)-2):
		if is_aba(line[i:i+3]):
			abas.add(line[i:i+3])

	return abas

def bab(aba):
	return aba[1] + aba[0] + aba[1]

def valid(line):
	line = line.replace('[', '(')
	line = line.replace(']', ')')

	brackets = re.findall(r'\([^()]*\)', line)
	line = re.sub(r'\([^()]*\)', '-', line)

	abas = get_abas(line)
	if len(abas) > 0:
		for aba in abas:
			for part in brackets:
				if bab(aba) in part:
					return True

	return False

print sum(1 for line in open('input.txt').readlines() if valid(line.strip()))