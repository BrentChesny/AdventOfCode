from itertools import combinations

types = ['TH', 'PL', 'ST', 'PR', 'RU']

def hash_config(config):
    global types
    
    hashcode = []
    current_floor, floors = config

    for type in types:
        generator_floor = [i for i in range(4) if type + 'G' in floors[i]][0]
        chip_floor = [i for i in range(4) if type + 'M' in floors[i]][0]

        hashcode.append((generator_floor, chip_floor))

    return (current_floor, tuple(sorted(hashcode)))

def end(conf):
    floor, floor_contents = conf
    return floor == 3 and len(floor_contents[0]) ==  len(floor_contents[1]) == len(floor_contents[2]) == 0

def valid(floor):
    if not any(item[-1] == 'G' for item in floor):
        return True

    for item in floor:
        if item[-1] == 'M':
            if not item[:-1] + 'G' in floor:
                return False

    return True


config = (
    0, # floor
    (
        tuple(sorted(('THG', 'THM', 'PLG', 'STG'))),
        tuple(sorted(('PLM', 'STM'))),
        tuple(sorted(('PRG', 'PRM', 'RUG', 'RUM'))),
        ()
    )
)


queue = [config]
visited = {hash_config(config) : 0}


while len(queue):
    conf = queue.pop(0)

    print visited[hash_config(conf)]

    if end(conf):
        break

    current_floor, floor_contents = conf

    directions = [direction for direction in [-1, 1] if 0 <= current_floor + direction <= 3]
    possible_moves = list(combinations(floor_contents[current_floor], 2)) + list(combinations(floor_contents[current_floor], 1))

    for move in possible_moves:
        for direction in directions:
            new_floors = list(floor_contents)
            new_floors[current_floor] = tuple([x for x in floor_contents[current_floor] if x not in move])
            new_floors[current_floor + direction] = tuple(sorted(floor_contents[current_floor + direction] + move))

            if valid(new_floors[current_floor]) and valid(new_floors[current_floor + direction]):
                new_config = (current_floor + direction, tuple(new_floors))

                if not hash_config(new_config) in visited:
                    visited[hash_config(new_config)] = visited[hash_config(conf)] + 1
                    queue.append(new_config)

    
