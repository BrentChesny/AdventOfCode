from itertools import combinations
import heapq

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
        tuple(sorted(('THG', 'THM', 'PLG', 'STG', 'ELG', 'ELM', 'DIG', 'DIM'))),
        tuple(sorted(('PLM', 'STM'))),
        tuple(sorted(('PRG', 'PRM', 'RUG', 'RUM'))),
        ()
    )
)


queue = []
heapq.heappush(queue, (0, config))
visited = {config : 0}

while len(queue):
    prio, conf = heapq.heappop(queue)
    

    if end(conf):
    	print visited[conf]
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

                new_steps = visited[conf] + 1
                if not new_config in visited or new_steps < visited[new_config]:
                    visited[new_config] = new_steps
                    heapq.heappush(queue, (new_steps - len(new_floors[3]), new_config))

    
