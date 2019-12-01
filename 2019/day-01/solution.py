from math import floor

def parse_input():
    return [int(line) for line in open('input.txt').readlines()]

def fuel(mass):
    return floor(mass / 3) - 2

def fuel_extra(mass):
    total_fuel = fuel(mass)
    fuel_fuel = fuel(total_fuel)
    while fuel_fuel > 0:
        total_fuel += fuel_fuel
        fuel_fuel = fuel(fuel_fuel)

    return total_fuel

def calculate_total_fuel(fuel_func, masses):
    return sum(map(fuel_func, parse_input()))

def solve_part_one():
    return calculate_total_fuel(fuel, parse_input())

def solve_part_two():
    return calculate_total_fuel(fuel_extra, parse_input())

def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())

if __name__ == '__main__':
    main()
