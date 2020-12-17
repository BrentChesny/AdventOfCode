from operator import add
from itertools import product


def parse_input(dim):
    alive = set()
    x, y = 0, 0
    for c in open("input.txt").read():
        if c == "#":
            coords = [x, y]
            while len(coords) < dim:
                coords.append(0)
            alive.add(tuple(coords))
        if c == "\n":
            x = 0
            y += 1
        else:
            x += 1
    return alive


def all_neighbours(alive, dim):
    return set.union(*[neighbours(p, dim) for p in alive])


def neighbours(p, dim):
    return {
        tuple(map(add, p, d))
        for d in product([-1, 0, 1], repeat=dim)
        if d != tuple(0 for _ in range(dim))
    }


def step(alive, dim):
    new_alive = set()
    for p in alive:
        n = neighbours(p, dim)
        alive_n = n.intersection(alive)
        if 2 <= len(alive_n) <= 3:
            new_alive.add(p)

    for n in all_neighbours(alive, dim):
        if n in alive:
            continue
        m = neighbours(n, dim)
        alive_m = m.intersection(alive)
        if len(alive_m) == 3:
            new_alive.add(n)

    return new_alive


def solve_part_one():
    alive = parse_input(3)
    for _ in range(6):
        alive = step(alive, 3)
    return len(alive)


def solve_part_two():
    alive = parse_input(4)
    for _ in range(6):
        alive = step(alive, 4)
    return len(alive)


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
