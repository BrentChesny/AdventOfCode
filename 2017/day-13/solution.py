def parse_input():
    firewall = dict()
    for line in open('input.txt').readlines():
        depth, rnge = map(int, line.strip().split(': '))
        firewall[depth] = rnge
    return firewall

def solve_part_one():
    firewall = parse_input()
    n = max(firewall.keys())
    severity = 0
    for tick in range(n+1):
        if tick in firewall and tick % ((firewall[tick] - 1) * 2) == 0:
            severity += tick * firewall[tick]

    return severity

def solve_part_two():
    firewall = parse_input()
    n = max(firewall.keys())
    delay = 0
    while True:
        for tick in range(n+1):
            if tick in firewall and (delay + tick) % ((firewall[tick] - 1) * 2) == 0:
                delay += 1
                break
        else:
            return delay

def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
