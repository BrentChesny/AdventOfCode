l = raw_input()
d = {'^' : (0,1), 'v' : (0,-1), '<' : (-1,0), '>' : (1,0)}
v = [(0,0)]
for x in l:
	v.append(tuple(map(sum, zip(v[-1], d[x]))))
print len(set(v))