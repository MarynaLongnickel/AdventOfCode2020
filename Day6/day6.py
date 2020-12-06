# --- Day 6: Custom Customs ---

from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2020/main/Day6/day6.txt').read().decode().split('\n\n')

print(sum(len(set(s.replace('\n',''))) for s in data))

# ---------------------- PART 2 ------------------------

print(sum(len(set.intersection(*(set(s) for s in d.split()))) for d in data))
