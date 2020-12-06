# --- Day 2: Password Philosophy ---

from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2020/main/Day2/day2.txt')
tot = 0

for n in data:
  r, l, p = n.decode().split()
  a, b = r.split('-')
  if p.count(l[0]) in range(int(a), int(b)+1):
    tot += 1

print(tot)

# ---------------------- PART 2 ------------------------

tot = 0

for n in data:
  r, l, p = n.decode().split()
  a, b = r.split('-')
  l, a, b = l[0], int(a) - 1, int(b) - 1
  if (p[a] == l and p[b] != l) or (p[a] != l and p[b] == l):
    tot += 1

print(tot)
