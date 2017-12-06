def solve_part_one():
    banks = map(int, open('input.txt').read().split())
    seen = set()
    rounds = 0

    while tuple(banks) not in seen:
        rounds += 1
        seen.add(tuple(banks))

        # Find bank with most blocks
        index, blocks = banks.index(max(banks)), max(banks)

        # Remove blocks from bank
        banks[index] = 0

        # Redistribute blocks
        while blocks:
            index = (index + 1) % len(banks)
            banks[index] += 1
            blocks -= 1

    return rounds

def solve_part_two():
    banks = map(int, open('input.txt').read().split())
    seen = dict()
    rounds = 0

    while tuple(banks) not in seen:
        rounds += 1
        seen[tuple(banks)] = rounds

        # Find bank with most blocks
        index, blocks = banks.index(max(banks)), max(banks)

        # Remove blocks from bank
        banks[index] = 0

        # Redistribute blocks
        while blocks:
            index = (index + 1) % len(banks)
            banks[index] += 1
            blocks -= 1

    return rounds - seen[tuple(banks)] + 1

def main():
    print 'Part one: ', solve_part_one()
    print 'Part two: ', solve_part_two()

if __name__ == '__main__':
    main()
