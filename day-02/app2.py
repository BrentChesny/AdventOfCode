l = [line.rstrip("\n").split("x") for line in open("input.txt")]
print sum([x[0]*x[1]*x[2] + 2*(sorted(x)[0]+sorted(x)[1]) for x in [map(int, z) for z in l]])