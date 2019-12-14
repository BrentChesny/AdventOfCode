import math
from collections import defaultdict


def parse_input():
    reactions = {}
    for line in open('input.txt'):
        start, end = line.strip().split(' => ')
        prereqs = []
        for s in start.split(', '):
            n, prod = s.split(' ')
            n = int(n)
            prereqs.append((n, prod))
        n, prod = end.split(' ')
        n = int(n)
        reactions[prod] = (prereqs, n)
    return reactions


def calc_ore_needed(n_fuel, reactions):
    inventory = defaultdict(int)
    ore_needed = 0

    prereqs, _ = reactions['FUEL']
    prereqs = multiply_ingredients(prereqs, n_fuel)

    while prereqs:
        needed, prod = prereqs.pop(0)
        if prod == 'ORE':
            ore_needed += needed
        else:
            if needed > inventory[prod]:
                needed -= inventory[prod]
                ingredients, gives = reactions[prod]
                reaction_times = math.ceil(needed / gives)
                prereqs.extend(multiply_ingredients(ingredients, reaction_times))
                inventory[prod] = (reaction_times * gives) - needed
            else:
                inventory[prod] -= needed
    return ore_needed


def multiply_ingredients(ingredients, n):
    return [(n * m, prod) for m, prod in ingredients]


def solve_part_one():
    reactions = parse_input()
    return calc_ore_needed(1, reactions)


def solve_part_two():
    reactions = parse_input()
    n_fuel = 0
    delta = 10**5
    while True:
        if calc_ore_needed(n_fuel, reactions) > 10**12:
            if delta == 1:
                return n_fuel - 1
            n_fuel -= delta
            delta //= 10
        n_fuel += delta


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
