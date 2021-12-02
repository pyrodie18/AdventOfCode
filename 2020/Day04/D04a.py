with open('./D04_Input.txt') as f:
    lines = [line.rstrip() for line in f]

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid_passports = 0
passport = {}
for line in lines:
    if len(line) > 0:
        elements = line.split(' ')
        for element in elements:
            key = element.split(':')
            passport[key[0]] = key[1]
    else:
        good_passport = True
        for field in fields:
            if field in passport:
                pass
            else:
                good_passport = False
        if good_passport:
            valid_passports = valid_passports + 1
        else:
            print(passport)
        passport = {}

print(valid_passports)