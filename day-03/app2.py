l = raw_input()
d = {'^' : (0,1), 'v' : (0,-1), '<' : (-1,0), '>' : (1,0)}
vs = [(0,0)]
vr = [(0,0)]
for i,x in enumerate(l):
	v = vs if i % 2 else vr
	v.append(tuple(map(sum, zip(v[-1], d[x]))))
print len(set(vs + vr))