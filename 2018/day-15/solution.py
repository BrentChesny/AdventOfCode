from collections import namedtuple, deque
from itertools import groupby, count

class Pos(namedtuple('Pos', ['row', 'col'])):
    def up(self):
        return Pos(self.row - 1, self.col, )

    def down(self):
        return Pos(self.row + 1, self.col)

    def left(self):
        return Pos(self.row, self.col - 1)

    def right(self):
        return Pos(self.row, self.col + 1)

    def adjacent(self):
        return [self.up(), self.left(), self.right(), self.down()]


class Unit:
    ELF = 'E'
    GOBLIN = 'G'

    def __init__(self, type, pos, power):
        self.type = type
        self.pos = pos
        self.hp = 200
        self.power = power

    def __repr__(self):
        return f'Unit(type={self.type}, pos={self.pos}, hp={self.hp})'

    def is_alive(self):
        return self.hp > 0

class Battlefield:
    def __init__(self, filename, elf_power = 3):
        self.parse_input(filename, elf_power)

    def display(self):
        grid = [row[:] for row in self.grid]
        for unit in self.units:
            if unit.is_alive():
                row, col = unit.pos
                grid[row][col] = unit.type
        for row in grid:
            print(''.join(row))
        for unit in self.units:
            print(unit)

    def parse_input(self, filename, elf_power):
        self.grid = []
        self.units = []

        for r, line in enumerate(open(filename).readlines()):
            row = []
            for c, char in enumerate(line.strip()):
                if char == Unit.ELF or char == Unit.GOBLIN:
                    if char == Unit.ELF:
                        power = elf_power
                    else:
                        power = 3
                    self.units.append(Unit(char, Pos(r, c), power))
                    row.append('.')
                else:
                    row.append(char)
            self.grid.append(row)


    def fight(self):
        completed_rounds = 0
        while True:
            if self.round():
                break
            completed_rounds += 1
        return completed_rounds * sum(unit.hp for unit in self.units if unit.is_alive())


    def round(self):
        self.units.sort(key= lambda u: u.pos)

        for unit in self.units:
            if not unit.is_alive():
                continue

            if not self.determine_targets(unit):
                return True

            self.attempt_move(unit)
            self.attempt_attack(unit)

    def attempt_move(self, unit):
        adjacent = unit.pos.adjacent()
        targets = self.determine_targets(unit)

        if any(t.pos in adjacent for t in targets):
            return

        in_range = [p for t in targets for p in t.pos.adjacent() if self.is_valid_pos(p)]
        new_pos = self.find_move_to_nearest(unit.pos, in_range)

        if not new_pos:
            return

        unit.pos = new_pos

    def attempt_attack(self, unit):
        adjacent = unit.pos.adjacent()
        targets_in_range = [t for t in self.determine_targets(unit) if t.pos in adjacent]

        if not targets_in_range:
            return

        chosen_target = min(targets_in_range, key=lambda unit: (unit.hp, unit.pos))

        chosen_target.hp -= unit.power

    def determine_targets(self, unit):
        return [u for u in self.units if u.is_alive() and u.type != unit.type]

    def is_valid_pos(self, pos):
        row, col= pos
        if self.grid[row][col] == '#':
            return False
        elif any(u.pos == pos and u.is_alive() for u in self.units):
            return False
        else:
            return True

    def find_move_to_nearest(self, start, targets):
        visiting = deque([(start, 0)])
        paths = {start: (0, None)}
        seen = set()

        while visiting:
            pos, dist = visiting.popleft()
            for next in pos.adjacent():
                if not self.is_valid_pos(next):
                    continue
                if next not in paths or paths[next] > (dist + 1, pos):
                    paths[next] = (dist + 1, pos)
                if next in seen:
                    continue
                if not any(next == visit[0] for visit in visiting):
                    visiting.append((next, dist + 1))
            seen.add(pos)

        reachable_targets = [(dist, pos) for pos, (dist, parent) in paths.items() if pos in targets]
        if not reachable_targets:
            return

        _, nearest = min(reachable_targets)
        while paths[nearest][0] > 1:
            nearest = paths[nearest][1]
        return nearest

    def has_dead_elves(self):
        return any(u.type == Unit.ELF and not u.is_alive() for u in self.units)


def solve_part_one():
    battlefield = Battlefield('input.txt')
    return battlefield.fight()


def solve_part_two():
    for power in count(4):
        battlefield = Battlefield('input.txt', power)
        outcome = battlefield.fight()
        if not battlefield.has_dead_elves():
            return outcome


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
