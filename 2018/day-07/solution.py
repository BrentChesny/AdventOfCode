import re
from collections import defaultdict

N_WORKERS = 5
TIME_BASE = 60

def parse_input():
    dependencies = defaultdict(set)
    all_parts = set()

    for line in open('input.txt'):
        x, y = re.match(r'Step (.) must be finished before step (.) can begin.', line).groups()
        dependencies[y].add(x)
        all_parts.update({x, y})

    for part in all_parts:
        if part not in dependencies:
            dependencies[part] = set()

    return dependencies

def part_time(part):
    return ord(part) - ord('A') + 1 + TIME_BASE

def solve_part_one():
    dependencies = parse_input()
    result = []

    while dependencies:
        available = [part for part, deps in dependencies.items() if not deps]
        chosen_part = min(available)
        result.append(chosen_part)

        for part, deps in dependencies.items():
            if chosen_part in deps:
                deps.remove(chosen_part)

        dependencies.pop(chosen_part)

    return ''.join(result)

def solve_part_two():
    dependencies = parse_input()
    time = 0

    workers = [None for _ in range(N_WORKERS)]

    while dependencies or any(workers):
        done_workers = [i for i in range(N_WORKERS) if workers[i] and workers[i][1] <= time]

        for i in done_workers:
            finished_part, end_time = workers[i]
            workers[i] = None

            for part, deps in dependencies.items():
                if finished_part in deps:
                    deps.remove(finished_part)

        available_parts = sorted([part for part, deps in dependencies.items() if not deps])
        available_workers = [i for i in range(N_WORKERS) if not workers[i]]

        for i in available_workers:
            if available_parts:
                part = available_parts.pop(0)
                workers[i] = (part, time + part_time(part))
                dependencies.pop(part)

        if any(workers):
            time = min(worker[1] for worker in workers if worker)

    return time


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
