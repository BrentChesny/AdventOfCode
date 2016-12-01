import re
content = open("input.txt", "r").read()
print sum(map(int, re.findall("(-?\d+)", content)))