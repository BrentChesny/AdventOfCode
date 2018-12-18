from itertools import count

N = 1000000000

class Grid:
    def __init__(self, filename):
        self.parse(filename)
        self.history = {}
        self.save(0)

    def parse(self, filename):
        self.grid = {}
        for row, line in enumerate(open(filename).readlines()):
            for col, element in enumerate(line.strip()):
                self.grid[(row, col)] = element

    def get(self, pos):
        return self.grid.get(pos, None)

    def adjacent(self, pos):
        adjacent = []
        row, col = pos
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr != 0 or dc != 0:
                    adjacent.append(self.get((row + dr, col + dc)))
        return list(filter(None, adjacent))

    def round(self, number):
        new_grid = {}
        for pos, element in self.grid.items():
            adj = self.adjacent(pos)
            if element == '.':
                new_grid[pos] = '|' if adj.count('|') >= 3 else element
            elif element == '|':
                new_grid[pos] = '#' if adj.count('#') >= 3 else element
            elif element == '#':
                new_grid[pos] = '.' if adj.count('#') == 0 or adj.count('|') == 0 else element
        self.grid = new_grid
        recall = self.recall()
        if recall:
            return recall
        else:
            self.save(number)

    def save(self, number):
        self.history[frozenset(self.grid.items())] = number

    def recall(self):
        h = frozenset(self.grid.items())
        if h in self.history:
            return self.history[h]

    def count(self, element):
        return len([e for e in self.grid.values() if e == element])

    def show(self):
        for row in range(50):
            print(''.join(self.grid[(row, col)] for col in range(50)))
        print()

    def __hash__(self):
        return hash(frozenset(self.grid.items()))



def solve_part_one():
    grid = Grid('input.txt')

    for current_round in range(1, 11):
        grid.round(current_round)

    return grid.count('|') * grid.count('#')

def solve_part_two():
    grid = Grid('input.txt')

    for current_round in count(1):
        previous_round = grid.round(current_round)
        if previous_round:
            delta = current_round - previous_round
            todo = (N - current_round) % delta
            break

    for i in range(todo):
        grid.round(i)

    return grid.count('|') * grid.count('#')


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
