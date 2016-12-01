l = [line.rstrip("\n").split("x") for line in open("input.txt")]
print sum([2*x[0]*x[1] + 2*x[1]*x[2] + 2*x[0]*x[2] + sorted(x)[0] * sorted(x)[1] for x in [map(int, z) for z in l]])