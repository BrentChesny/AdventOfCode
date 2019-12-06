from collections import defaultdict


def parse_input():
    orbits = [line.strip().split(')') for line in open('input.txt').readlines()]

    orbited_by = defaultdict(list)
    for orbitee, orbiter in orbits:
        orbited_by[orbitee].append(orbiter)

    orbiting = dict()
    for orbitee, orbiter in orbits:
        orbiting[orbiter] = orbitee
    return orbited_by, orbiting


def get_total_orbiters(object, orbited_by):
    if object not in orbited_by:
        return 0
    orbiters = orbited_by[object]
    return len(orbiters) + sum(map(lambda o: get_total_orbiters(o, orbited_by), orbiters))


def solve_part_one():
    orbited_by, _ = parse_input()
    return sum(map(lambda o: get_total_orbiters(o, orbited_by), orbited_by.keys()))


def solve_part_two():
    orbited_by, orbiting = parse_input()
    start = orbiting['YOU']
    end = orbiting['SAN']

    reachable = {start}
    steps = 0
    while end not in reachable:
        steps += 1
        for r in reachable.copy():
            for o in orbited_by[r]:
                reachable.add(o)
            reachable.add(orbiting[r])
    return steps


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
