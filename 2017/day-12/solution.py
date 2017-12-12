def parse_input():
    network = dict()
    for line in open('input.txt').readlines():
        source, dests = line.strip().split(' <-> ')
        source = int(source)
        dests = map(int, dests.split(', '))
        network[source] = dests

    return network

def solve_part_one():
    network = parse_input()

    return len(calculate_group(0, network))

def solve_part_two():
    network = parse_input()
    nodes = network.keys()

    result = 0
    while nodes:
        node = nodes.pop(0)
        group = calculate_group(node, network)
        for x in group:
            if x in nodes:
                nodes.remove(x)
        result += 1

    return result

def calculate_group(source, network):
    group = {source}
    n = 0
    while len(group) != n:
        n = len(group)
        for source, dests in network.items():
            if source in group:
                group |= set(dests)

    return group


def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
