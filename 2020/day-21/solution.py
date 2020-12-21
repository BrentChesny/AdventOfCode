import re

regex = re.compile("(.*) \(contains (.*)\)")


def parse_input():
    foods = []
    for line in open("input.txt").read().splitlines():
        ingredients, allergens = regex.match(line).groups()
        foods.append((set(ingredients.split(" ")), set(allergens.split(", "))))
    return foods


def find_ingredients_with_allergens(foods):
    all_allergens = set(a for _, allergens in foods for a in allergens)

    possible_ingredients_with_allergens = dict()

    for allergen in all_allergens:
        options = []
        for ingredients, allergens in foods:
            if allergen in allergens:
                options.append(ingredients)
        possible_ingredients_with_allergens[allergen] = set.intersection(*options)

    decided = {
        list(ingredients)[0]
        for ingredients in possible_ingredients_with_allergens.values()
        if len(ingredients) == 1
    }

    while True:
        for ingredients in possible_ingredients_with_allergens.values():
            if len(ingredients) > 1:
                ingredients.difference_update(decided)
        old_decided = decided
        decided = {
            list(ingredients)[0]
            for ingredients in possible_ingredients_with_allergens.values()
            if len(ingredients) == 1
        }
        if len(old_decided) == len(decided):
            break

    return {
        allergen: list(ingredients)[0]
        for allergen, ingredients in possible_ingredients_with_allergens.items()
    }


def solve_part_one():
    foods = parse_input()
    ingredients_with_allergens = find_ingredients_with_allergens(foods)

    occs = 0
    for ingredients, _ in foods:
        occs += len(
            set(ingredients).difference(set(ingredients_with_allergens.values()))
        )
    return occs


def solve_part_two():
    foods = parse_input()
    ingredients_with_allergens = find_ingredients_with_allergens(foods)

    allergens = ingredients_with_allergens.keys()
    return ",".join(
        ingredients_with_allergens[allergen] for allergen in sorted(allergens)
    )


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
