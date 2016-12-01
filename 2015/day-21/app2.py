import re

boss = [int(re.findall('([\d]+)', line)[0]) for line in open('input.txt')]

weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
armors 	= [(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
rings 	= [(0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

def fight(attack, defense, boss):
	hp = 100
	boss_hp, boss_attack, boss_defense = boss
	player_turn = True
	while hp > 0 and boss_hp > 0:
		if player_turn:
			boss_hp -= max(attack - boss_defense, 1)
		else:
			hp -= max(boss_attack - defense, 1)
		player_turn = not player_turn
	
	return hp > 0

costs = []

for weapon in weapons:
	for armor in armors:
		for ring1 in rings:
			for ring2 in rings:
				cost = weapon[0] + armor[0] + ring1[0] + ring2[0]
				attack = weapon[1] + armor[1] + ring1[1] + ring2[1]
				defense = weapon[2] + armor[2] + ring1[2] + ring2[2]

				if not fight(attack, defense, boss[:]):
					costs.append(cost)

print max(costs)