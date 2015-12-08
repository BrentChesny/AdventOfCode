print sum([len(x.replace("\\", "\\\\").replace("\"", "\\\""))+2-len(x) for x in [line.rstrip("\n") for line in open("input.txt")]])
