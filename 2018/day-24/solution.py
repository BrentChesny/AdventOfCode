import re
from pprint import pprint

IMMUNE_SYSTEM = 'immune_system'
INFECTION = 'infection'

class Group:
    def __init__(self, army, idx, units, hp, weaknesses, immunities, attack_damage, attack_type, initiative):
        self.army = army
        self.idx = idx
        self.units = units
        self.hp = hp
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.attack_damage = attack_damage
        self.attack_type = attack_type
        self.initiative = initiative

    def __repr__(self):
        return f'Group(army={self.army}, units={self.units}, hp={self.hp}, weaknesses={self.weaknesses}, immunities={self.immunities}, attack_damage={self.attack_damage}, attack_type={self.attack_type}, initiative={self.initiative})'

    def __hash__(self):
        return hash((self.army, self.idx))

    def __eq__(self, other):
        if other == None:
            return False
        return (self.army, self.idx) == (other.army, other.idx)

class StalemateError(Exception):
    pass

def parse_input(boost):
    immune_system, infection = open('input.txt').read().strip().split('\n\n')
    immune_system, infection = immune_system.split('\n'), infection.split('\n')
    immune_system = immune_system[1:]
    infection = infection[1:]
    immune_system = [parse_group(line, IMMUNE_SYSTEM, i, boost) for i, line in enumerate(immune_system)]
    infection = [parse_group(line, INFECTION, i, boost) for i, line in enumerate(infection)]
    return immune_system + infection

def parse_group(line, army, idx, boost):
    units = int(re.match(r'(\d+) units', line).groups()[0])
    hp = int(re.match(r'.* (\d+) hit points', line).groups()[0])
    match = re.match(r'.* (\(.*\)) .*', line)
    weaknesses = []
    immunities = []
    if match:
        groups = match.groups()
        things = groups[0][1:-1].split('; ')
        for thing in things:
            parts = thing.split(' ')
            if parts[0] == 'immune':
                for p in parts[2:]:
                    immunities.append(p.strip(','))
            elif parts[0] == 'weak':
                for p in parts[2:]:
                    weaknesses.append(p.strip(','))
    groups = re.match(r'.* (\d+) ([a-z]+) damage', line).groups()
    attack_damage = int(groups[0]) + (boost if army == IMMUNE_SYSTEM else 0)
    attack_type =  groups[1]
    initiative = int(re.match(r'.* initiative (\d+)', line).groups()[0])
    return Group(army, idx, units, hp, weaknesses, immunities, attack_damage, attack_type, initiative)

def effective_power(group):
    return group.units * group.attack_damage

def potential_damage(attacker, target):
    damage = effective_power(attacker)
    if attacker.attack_type in target.immunities:
        damage = 0
    elif attacker.attack_type in target.weaknesses:
        damage *= 2
    return damage

def simulate_fight(boost = 0):
    groups = parse_input(boost)

    while True:
        # Target selection
        groups.sort(key=lambda g: (effective_power(g), g.initiative), reverse=True)
        targets = {}
        for attacker in groups:
            if attacker.units <= 0:
                continue
            potential_targets = [potential_target for potential_target in groups if attacker.army != potential_target.army and potential_target.units > 0 and potential_target not in targets.values() and potential_damage(attacker, potential_target) > 0]
            target = max(potential_targets, key=lambda t: (potential_damage(attacker, t), effective_power(t), t.initiative), default=None)
            targets[attacker] = target

        # Attacking
        groups.sort(key=lambda g: g.initiative, reverse=True)
        total_kills = 0
        for attacker in groups:
            if attacker.units <= 0:
                continue
            target = targets[attacker]
            if target == None:
                continue
            damage = potential_damage(attacker, target)
            killed = min(damage // target.hp, target.units)
            total_kills += killed
            target.units -= killed

        if total_kills == 0:
            raise StalemateError()

        # Is it over?
        if sum([g.units for g in groups if g.army == IMMUNE_SYSTEM]) == 0 or sum([g.units for g in groups if g.army == INFECTION]) == 0:
            return groups

def solve_part_one():
    result = simulate_fight()
    return sum(g.units for g in result)

def solve_part_two():
    for boost in range(1010):
        try:
            result = simulate_fight(boost)
        except StalemateError:
            continue
        if sum([g.units for g in result if g.army == IMMUNE_SYSTEM]) > 0:
            return sum(g.units for g in result)


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
