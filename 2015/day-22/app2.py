import re

boss = [int(re.findall('([\d]+)', line)[0]) for line in open('input.txt')]
spells = {"missile" : 53, "drain" : 73, "shield" : 113, "poison" : 173, "recharge" : 229}
min_cost = 9999999

def fight(player_hp, mana, boss_hp, boss_damage, spell, timer_shield, timer_poison, timer_recharge, cost):
	global min_cost

	if cost > min_cost:
		return

	if spells[spell] > mana:
		return

	for turn in [0, 1]:
		armor = 0

		if turn == 0:
			player_hp -= 1
		
		# shield effect active
		if timer_shield > 0:
			armor = 7
			timer_shield -= 1

		# poison effect active
		if timer_poison > 0:
			boss_hp -= 3
			timer_poison -= 1

		# recharge effect active
		if timer_recharge > 0:
			mana += 101
			timer_recharge -= 1

		# check for death
		if player_hp <= 0:
			return
		elif boss_hp <= 0:
			min_cost = min(min_cost, cost)
			return

		# player's turn or boss' turn
		if turn == 0:
			if spell == "missile":
				boss_hp -= 4
			elif spell == "drain":
				boss_hp -= 2
				player_hp += 2
			elif spell == "shield":
				if timer_shield > 0:
					return
				else:
					timer_shield = 6
			elif spell == "poison":
				if timer_poison > 0:
					return
				else:
					timer_poison = 6
			elif spell == "recharge":
				if timer_recharge > 0:
					return
				else:
					timer_recharge = 5
			mana -= spells[spell]
			cost += spells[spell]
		else:
			player_hp -= max(boss_damage - armor, 1)

		# check for death
		if player_hp <= 0:
			return
		elif boss_hp <= 0:
			min_cost = min(min_cost, cost)
			return


	for s in spells:
		fight(player_hp, mana, boss_hp, boss_damage, s, timer_shield, timer_poison, timer_recharge, cost)


for s in spells:
	fight(50, 500, boss[0], boss[1], s, 0, 0, 0, 0)

print min_cost