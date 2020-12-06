# --- Day 5: Binary Boarding ---

from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2020/main/Day5/day5.txt').read().decode().split('\n')[:-1]
# data = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL'] # sample data

x = 0
ids = []

for d in data:
    r, c = range(128), range(8)
    for i in range(7):
        r = r[:int(len(r)/2)] if d[i] == 'F' else r[int(len(r)/2):]
    for i in range(7,10):
        c = c[:int(len(c)/2)] if d[i] == 'L' else c[int(len(c)/2):]
    s = r[0]*8 + c[0]
    if s > x:
        x = s
    ids.append(s)

print(x)
print(set(range(x)) - set(ids))
