import re
from math import gcd
from functools import reduce

regex = re.compile('<x=(\-?\d+), y=(\-?\d+), z=(\-?\d+)>')


def parse_input():
    return [tuple(map(int, regex.match(line).groups())) for line in open('input.txt')]


def step_dimension(positions, velocities):
    new_positions = positions[:]
    new_velocities = velocities[:]

    for i in range(len(positions)):
        vxi = velocities[i]
        xi = positions[i]

        for j in range(len(positions)):
            if i != j:
                xj = positions[j]

                vxi += -1 if xi > xj else 1 if xi < xj else 0

        new_velocities[i] = vxi
        new_positions[i] = xi + vxi

    return new_positions, new_velocities


def simulate_dimension(starting_positions, steps):
    positions = starting_positions
    velocities = [0 for p in positions]

    for s in range(steps):
        positions, velocities = step_dimension(positions, velocities)

    return positions, velocities


def simulate(starting_positions, steps):
    xs, ys, zs = map(list, zip(*starting_positions))

    xs, vxs = simulate_dimension(xs, steps)
    ys, vys = simulate_dimension(ys, steps)
    zs, vzs = simulate_dimension(zs, steps)

    return list(zip(xs, ys, zs)), list(zip(vxs, vys, vzs))


def find_repetition_dimension(starting_positions):
    positions = starting_positions
    velocities = [0 for p in positions]
    seen = set()
    step_count = 0

    while (tuple(positions), tuple(velocities)) not in seen:
        seen.add((tuple(positions), tuple(velocities)))
        positions, velocities = step_dimension(positions, velocities)
        step_count += 1

    return step_count


def lcm(*args):
    return reduce(lambda a, b: a * b // gcd(a, b), args)


def find_repetition(starting_positions):
    xs, ys, zs = map(list, zip(*starting_positions))

    rep_x = find_repetition_dimension(xs)
    rep_y = find_repetition_dimension(ys)
    rep_z = find_repetition_dimension(zs)

    return lcm(rep_x, rep_y, rep_z)


def total_energy(positions, velocities):
    return sum(sum(map(abs, p)) * sum(map(abs, v)) for p, v in zip(positions, velocities))


def solve_part_one():
    moons = parse_input()
    positions, velocities = simulate(moons, 1000)
    return total_energy(positions, velocities)


def solve_part_two():
    moons = parse_input()
    return find_repetition(moons)


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
