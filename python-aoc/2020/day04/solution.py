from typing import List
inp: List[str] = open("2020/day04/input.txt").read().split("\n\n")

passports = [{category[0]: category[1] for category in [x.split(":") for x in chunk.replace("\n", " ").split(" ")]} for chunk in inp]  # wild

# p1
valid = 0
for passport in passports:
    if len(passport) == 8:
        valid += 1
    elif len(passport) == 7 and "cid" not in passport:
        valid += 1
print("P1:", valid)

# p2
valid = 0
for passport in passports:
    if len(passport) == 8 or (len(passport) == 7 and "cid" not in passport):
        if (
            (1920 <= int(passport["byr"]) and int(passport["byr"]) <= 2002)
            and (2010 <= int(passport["iyr"]) and int(passport["iyr"]) <= 2020)
            and (2020 <= int(passport["eyr"]) and int(passport["eyr"]) <= 2030)
            and ( ( (passport["hgt"][-2:] == "cm") and ( 150 <= int(passport["hgt"][:-2]) and int(passport["hgt"][:-2]) <= 193))
                or ( (passport["hgt"][-2:] == "in") and ( 59 <= int(passport["hgt"][:-2]) and int(passport["hgt"][:-2]) <= 76)))
            and ( (passport["hcl"][0] == "#") and (0 not in [x in "1234567890abcdef"for x in passport["hcl"][1:] ]) and (len(passport["hcl"][1:]) == 6))
            and (passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
            and ((len(passport["pid"])==9) and (passport["pid"].isdigit()))
        ):
            valid += 1

print("P2:", valid)