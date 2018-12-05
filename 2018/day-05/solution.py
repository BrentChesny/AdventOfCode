from string import ascii_lowercase, ascii_uppercase

def parse_input():
    return open('input.txt').read().strip()

def generate_reactive_units():
    reactives_a = [x + y for x, y in zip(ascii_lowercase, ascii_uppercase)]
    reactives_b = [x + y for x, y in zip(ascii_uppercase, ascii_lowercase)]
    return reactives_a + reactives_b

def react_polymer(polymer):
    reactives = generate_reactive_units()

    while True:
        indices = {reactive: polymer.find(reactive) for reactive in reactives}
        filtered_indices = list(filter(lambda x: x[1] != -1, indices.items()))
        if not filtered_indices:
            break
        reactive, idx = min(filtered_indices, key=lambda x: x[1])
        polymer = polymer.replace(reactive, '', 1)

    return polymer


def solve_part_one():
    return len(react_polymer(parse_input()))

def solve_part_two():
    polymer = parse_input()
    polymer_lengths = []

    for unit in ascii_lowercase:
        new_polymer = polymer.replace(unit, '').replace(unit.upper(), '')
        polymer_lengths.append(len(react_polymer(new_polymer)))

    return min(polymer_lengths)


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
