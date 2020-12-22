def parse_input():
    player1, player2 = open("input.txt").read().split("\n\n")
    deck1 = [int(line) for line in player1.splitlines()[1:]]
    deck2 = [int(line) for line in player2.splitlines()[1:]]
    return deck1, deck2


def score(cards):
    return sum((i + 1) * card for i, card in enumerate(reversed(cards)))


def solve_part_one():
    deck1, deck2 = parse_input()

    while deck1 and deck2:
        a, deck1 = deck1[0], deck1[1:]
        b, deck2 = deck2[0], deck2[1:]

        if a > b:
            deck1 += [a, b]
        else:
            deck2 += [b, a]

    return score(deck1) if deck1 else score(deck2)


def play(deck1, deck2):
    seen = set()

    while deck1 and deck2:
        serialized = (tuple(deck1), tuple(deck2))
        if serialized in seen:
            return 1, -1
        seen.add(serialized)
        a, deck1 = deck1[0], deck1[1:]
        b, deck2 = deck2[0], deck2[1:]

        if a <= len(deck1) and b <= len(deck2):
            winner, _ = play(deck1[:a], deck2[:b])
        else:
            winner = 1 if a > b else 2

        if winner == 1:
            deck1 += [a, b]
        else:
            deck2 += [b, a]

    return 1 if deck1 else 2, score(deck1) if deck1 else score(deck2)


def solve_part_two():
    deck1, deck2 = parse_input()
    _, score = play(deck1, deck2)
    return score


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
