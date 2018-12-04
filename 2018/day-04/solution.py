import re
from collections import defaultdict, Counter
from operator import itemgetter


def parse_action(line):
    if 'wakes up' in line:
        return 'wake'
    elif 'falls asleep' in line:
        return 'sleep'
    else:
        return 'change'


def parse_input():
    records = []

    for line in open('input.txt'):
        matches = list(map(int, re.findall(r'\d+', line)))

        if len(matches) == 6:
            action, time, guard = parse_action(line), matches[:-1], matches[-1]
        else:
            action, time, guard = parse_action(line), matches, None
        records.append((tuple(time), action, guard))

    return sorted(records, key=itemgetter(0))


def process_records():
    current_guard = None
    total_sleep_per_guard = defaultdict(int)
    minutes_sleeping = defaultdict(list)
    start_sleep = None

    for time, action, guard in parse_input():
        _, _, _, h, m = time
        if action == 'change':
            current_guard = guard
        elif action == 'sleep':
            start_sleep = m
        elif action == 'wake':
            total_sleep_per_guard[current_guard] += m - start_sleep
            minutes_sleeping[current_guard].extend(list(range(start_sleep, m)))
            start_sleep = None

    minute_counts_per_guard = {
        guard: Counter(minutes)
        for guard, minutes in minutes_sleeping.items()
    }

    return total_sleep_per_guard, minute_counts_per_guard


def solve_part_one():
    total_sleep_per_guard, minute_counts_per_guard = process_records()

    most_sleeping_guard = max(total_sleep_per_guard.items(), key=itemgetter(1))[0]
    minute_most_slept = minute_counts_per_guard[most_sleeping_guard].most_common(1)[0][0]

    return most_sleeping_guard * minute_most_slept


def solve_part_two():
    total_sleep_per_guard, minute_counts_per_guard = process_records()

    most_sleeping_guard, most_sleeping_minute, max_count = None, None, 0

    for guard, minute_counts in minute_counts_per_guard.items():
        for minute, count in minute_counts.items():
            if count > max_count:
                most_sleeping_guard = guard
                most_sleeping_minute = minute
                max_count = count

    return most_sleeping_guard * most_sleeping_minute



def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
