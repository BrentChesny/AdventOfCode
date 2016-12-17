from hashlib import md5

directions = [('U', (0, -1)), ('D', (0, 1)), ('L', (-1, 0)), ('R', (1, 0))]
puzzle_input = 'pvhmgsws'

queue = [(0, (0, 0), '')]

def open_doors(path):
	hashcode = md5(puzzle_input + path).hexdigest()[:4]
	return [directions[i] for i, char in enumerate(hashcode) if char in 'bcdef']



while queue:
	steps, pos, path = queue.pop(0)

	moves = open_doors(path)
	for move in moves:
		door, dpos = move
		new_path = path + door
		new_steps = steps + 1
		new_pos_x, new_pos_y = pos[0] + dpos[0], pos[1] + dpos[1]

		if 0 <= new_pos_x <= 3 and 0 <= new_pos_y <= 3:
			new_pos = (new_pos_x, new_pos_y)
			if new_pos == (3, 3):
				print new_steps
			else:
				queue.append((new_steps, new_pos, new_path))




