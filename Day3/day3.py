# --- Day 3: Toboggan Trajectory ---

from urllib.request import urlopen
from numpy import prod

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2020/main/Day3/day3.txt').read().decode().split('\n')[:-1]

def get_trees(slope):
    tot = 0
    x, y = slope

    while y < len(data):
        if data[y][x % len(data[0])] == '#':
            tot += 1
        x += slope[0]
        y += slope[1]

    return tot

print(get_trees([3, 1]))

# ---------------------- PART 2 ------------------------

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

t = prod([get_trees(s) for s in slopes])
