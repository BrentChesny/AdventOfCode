import re


def parse_input():
    passports = []
    current_passport = []
    for line in open("input.txt"):
        line = line.strip()
        if line == "":
            passports.append([tuple(entry.split(":")) for entry in current_passport])
            current_passport = []
        else:
            current_passport.extend(line.split(" "))
    passports.append([tuple(entry.split(":")) for entry in current_passport])
    return passports


def validate_height(v):
    if v[-2:] == "cm":
        return 150 <= int(v[:-2]) <= 193
    elif v[-2:] == "in":
        return 59 <= int(v[:-2]) <= 76
    return False


NORTH_POLE_CREDENTIAL_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
COLOR_PATTERN = re.compile("^#([0-9a-f]){6}$")
PID_PATTERN = re.compile("^([0-9]){9}$")
VALIDATE = {
    "byr": lambda v: 1920 <= int(v) <= 2002,
    "iyr": lambda v: 2010 <= int(v) <= 2020,
    "eyr": lambda v: 2020 <= int(v) <= 2030,
    "hgt": validate_height,
    "hcl": lambda v: COLOR_PATTERN.match(v) != None,
    "ecl": lambda v: v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda v: PID_PATTERN.match(v) != None,
    "cid": lambda v: True,
}


def solve_part_one():
    passports = parse_input()
    count = 0
    for passport in passports:
        fields = set(f for f, _ in passport)
        if NORTH_POLE_CREDENTIAL_FIELDS.issubset(fields):
            count += 1
    return count


def solve_part_two():
    passports = parse_input()
    count = 0
    for passport in passports:
        passport_map = {f: v for f, v in passport}
        fields = set(passport_map.keys())
        if NORTH_POLE_CREDENTIAL_FIELDS.issubset(fields):
            valid = True
            for f, v in passport_map.items():
                if not VALIDATE[f](v):
                    valid = False
            if valid:
                count += 1
    return count


def main():
    print("Part one: ", solve_part_one())
    print("Part two: ", solve_part_two())


if __name__ == "__main__":
    main()
