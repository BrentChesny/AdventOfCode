size = 10000
prev = 20151125

for k in xrange(0,size*2):
	for j in xrange(0,k+1):
		i = k - j
		if i < size and j < size:
			if i == 2980 and j == 3074:
				print i, j, prev
			prev = (prev * 252533) % 33554393
