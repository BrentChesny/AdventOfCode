N = 1000

def parse_rule(line):
    pre, post = line.split(' => ')
    return (tuple(pre), post)

def parse_input():
    lines = [line.strip() for line in open('input.txt')]
    initial_state = list(lines[0].replace('initial state: ', ''))
    rules = dict([parse_rule(line) for line in lines[2:]])
    return initial_state, rules

def calculate_sum(state, offset):
    return sum(i-offset for i, pot in enumerate(state) if pot == '#')


def solve_part_one():
    state, rules = parse_input()
    offset = 0

    for _ in range(20):
        state = list('...') + state + list('...')
        new_state = ['.' for _ in state]
        offset += 3
        for i in range(2, len(state) - 2):
            slice = state[i-2:i+3]
            plant = rules[tuple(slice)]
            new_state[i] = plant
        state = new_state

    return calculate_sum(state, offset)

def solve_part_two():
    state, rules = parse_input()
    offset = 0
    last_sum = calculate_sum(state, offset)

    for _ in range(N):
        state = list('...') + state + list('...')
        new_state = ['.' for _ in state]
        offset += 3
        for i in range(2, len(state) - 2):
            slice = state[i-2:i+3]
            plant = rules[tuple(slice)]
            new_state[i] = plant
        state = new_state

        sum = calculate_sum(state, offset)
        diff = sum - last_sum
        last_sum = sum

    return last_sum + (50000000000 - N) * diff

def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
