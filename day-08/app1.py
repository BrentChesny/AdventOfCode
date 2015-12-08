print sum([len(x) - len(eval(x)) for x in [line.rstrip("\n") for line in open("input.txt")]])
