import re
from networkx import Graph, find_cliques
from collections import namedtuple

Bot = namedtuple('Bot', ['x', 'y', 'z', 'r'])

def parse_input():
    return [Bot(*map(int, re.findall(r'\-?\d+', line))) for line in open('input.txt')]

def dist(bot, other):
    return abs(bot.x - other.x) + abs(bot.y - other.y) + abs(bot.z - other.z)

def solve_part_one():
    bots = parse_input()

    strongest = max(bots, key=lambda bot: bot.r)

    result = 0
    for bot in bots:
        d = dist(strongest, bot)
        if d <= strongest.r:
            result += 1
    return result


def solve_part_two():
    bots = parse_input()

    graph = Graph()
    for bot in bots:
        for other in bots:
            if dist(bot, other) <= bot.r + other.r:
                graph.add_edge(bot, other)

    clique = max(find_cliques(graph), key=len)

    return max(dist(Bot(0, 0, 0, 0), bot) - bot.r for bot in clique)


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
