INPUT = 540391

def solve_part_one():
    recipes = '37'
    elf1, elf2 = 0, 1

    while len(recipes) < INPUT + 10:
        r1, r2 = int(recipes[elf1]), int(recipes[elf2])
        new_recipe = r1 + r2
        recipes += str(new_recipe)
        elf1 = (elf1 + 1 + r1) % len(recipes)
        elf2 = (elf2 + 1 + r2) % len(recipes)

    return recipes[INPUT:INPUT + 10]


def solve_part_two():
    recipes = '37'
    elf1, elf2 = 0, 1
    input_str = str(INPUT)

    while True:
        r1, r2 = int(recipes[elf1]), int(recipes[elf2])
        new_recipe = r1 + r2
        recipes += str(new_recipe)
        elf1 = (elf1 + 1 + r1) % len(recipes)
        elf2 = (elf2 + 1 + r2) % len(recipes)

        if recipes[-len(input_str):] == input_str or recipes[-len(input_str) - 1:-1] == input_str:
            return recipes.index(input_str)


def main():
    print('Part one: ', solve_part_one())
    print('Part two: ', solve_part_two())


if __name__ == '__main__':
    main()
