# --- Day 4: Passport Processing ---

from urllib.request import urlopen
import re

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2020/main/Day4/day4.txt').read().decode().split('\n\n')
fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
tot = 0

for p in data:
    check = [f in p for f in fields]
    if all(check):
        tot += 1

print(tot)

# ---------------------- PART 2 ------------------------

tot = 0

for p in data:
    check = [f in p for f in fields]
    if all(check):
        p = {x.split(':')[0] : x.split(':')[1] for x in re.split('\n| ', p) if ':' in x}
        
        if ((1920 <= int(p['byr']) <= 2002) and
           (2010 <= int(p['iyr']) <= 2020) and
           (2020 <= int(p['eyr']) <= 2030) and
           (((p['hgt'][-2:] == 'cm') and (150 <= int(p['hgt'][:-2]) <= 193)) or
            ((p['hgt'][-2:] == 'in') and (59 <= int(p['hgt'][:-2]) <= 76))) and
           (p['hcl'][0] == '#' and all([x.isalnum() for x in p['hcl'][1:]])) and
           (p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) and
           (len(p['pid']) == 9 and all([x.isdigit() for x in p['pid']]))):
           tot += 1
           
print(tot)
