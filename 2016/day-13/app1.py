puzzle_input = 1362

directions = [(0,1), (0,-1), (1,0), (-1,0)]
visited = {(1,1)}

queue = [(0,1,1)]

def valid(x,y):
    n = x*x + 3*x + 2*x*y + y + y*y + puzzle_input
    ones = bin(n).count('1')
    return ones % 2 == 0

while queue:
    steps, x, y = queue.pop(0)

    if (x,y) == (31,39):
        print steps
        break

    for dx, dy in directions:
        newx, newy = (x + dx, y + dy)

        if newx >= 0 and newy >= 0 and valid(newx, newy) and (newx,newy) not in visited:
            visited.add((newx,newy))
            queue.append((steps + 1, newx, newy))
