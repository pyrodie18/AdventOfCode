import re

with open('./Day04/D04_Input.txt') as f:
    lines = [line.rstrip() for line in f]

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def check_byr(passport):
    valid = False

    try:
        value = passport['byr']
    except:
        return valid
    year = re.findall("^\d{4}$", value)
    if len(year) == 1:
        if (int(year[0]) >= 1920) and (int(year[0]) <= 2002):
            valid = True
    return valid

def check_iyr(passport):
    valid = False

    try:
        value = passport['iyr']
    except:
        return valid
    year = re.findall('^\d{4}$', value)
    if len(year) == 1:
        if (int(year[0]) >= 2010) and (int(year[0]) <= 2020):
            valid = True
    return valid

def check_eyr(passport):
    valid = False

    try:
        value = passport['eyr']
    except:
        return valid
    year = re.findall('^\d{4}$', value)
    if len(year) == 1:
        if (int(year[0]) >= 2020) and (int(year[0]) <= 2030):
            valid = True
    return valid

def check_hgt(passport):
    valid = False

    try:
        value = passport['hgt']
    except:
        return valid
    height = re.findall("^(\d{3})cm$", value)
    if len(height) == 1:
        value = int(height[0])
        if (value >= 150) and (value <= 193):
            valid = True
    else:
        height = re.findall("^(\d{2})in$", value)
        if len(height) == 1:
            value = int(height[0])
            if (value >= 59) and (value <= 76):
                valid = True
    return valid

def check_hcl(passport):
    valid = False

    try:
        value = passport['hcl']
    except:
        return valid
    color = re.findall('^#[0-9a-f]{6}$', value)
    if len(color) == 1:
        valid = True
    return valid

def check_ecl(passport):
    valid = False

    try:
        value = passport['ecl']
    except:
        return valid
    color = re.findall('^(amb|blu|brn|gry|grn|hzl|oth)$', value)
    if len(color) == 1:
        valid = True
    return valid

def check_pid(passport):
    valid = False

    try:
        value = passport['pid']
    except:
        return valid
    value = re.findall('^\d{9}$', value)
    if len(value) == 1:
        valid = True

    if not valid:
        print(passport)
    return valid




valid_passports = 0
passports = []
passport = {}
for line in lines:
    if len(line) > 0:
        elements = line.split(' ')
        for element in elements:
            key = element.split(':')
            passport[key[0]] = key[1]
    else:
        passports.append(passport)
        passport = {}



for passport in passports:
    valid = False
    if check_byr(passport):
        if check_iyr(passport):
            if check_eyr(passport):
                if check_hgt(passport):
                    if check_hcl(passport):
                        if check_ecl(passport):
                            if check_pid(passport):
                                valid = True

    if valid:
        valid_passports = valid_passports + 1
print(valid_passports)

