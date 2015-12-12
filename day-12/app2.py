import json

data = json.load(open("input.txt", "r"))

def a(v):
	if isinstance(v, dict) and "red" not in v.values():
		return sum(map(a, v.values()))
	elif isinstance(v, list):
		return sum(map(a, v))
	elif isinstance(v, int):
		return v
	else:
		return 0

print a(data)