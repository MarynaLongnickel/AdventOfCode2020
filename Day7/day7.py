# --- Day 7: Handy Haversacks ---

from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2020/main/Day7/day7.txt').read().decode().split('\n')[:-1]
dic = {}

for d in data:
    d = d.split(' bags contain ')
    k = d[0]
    v = d[1].replace('s, ', '').replace('s.', '').replace(', ', '').split('bag')[:-1]
    v = [x[2:-1] for x in v if x != 'no other ']
    for i in v:
        if i not in dic.keys():
            dic[i] = []
        dic[i].append(k)

q = ['shiny gold']
found = []

while q:
    bag = q.pop()
    if bag in dic.keys():
        for i in dic[bag]:
            if i not in found:
                found.append(i)
                q.append(i)

print(len(found))

# ---------------------- PART 2 ------------------------

dic = {}

for d in data:
    d = d.split(' bags contain ')
    k = d[0]
    v = d[1].replace('s, ', '').replace('s.', '').replace(', ', '').split('bag')[:-1]
    v = [x[:-1] for x in v if x != 'no other ']
    dic[k] = v

def count_bags(b):
    if len(dic[b[2:]]) > 0:
        tot = 0
        for i in dic[b[2:]]:
            tot += int(i[0]) + int(i[0]) * count_bags(i)
        return tot
    else:
        return 0

print(count_bags('1 shiny gold'))
