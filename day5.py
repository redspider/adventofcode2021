import itertools
from collections import defaultdict

INPUT = open('5.input').read()

coords = defaultdict(int)


def full_range(a, b):
    if a < b:
        return range(a, b + 1)
    return range(a, b - 1, -1)


for line in INPUT.split("\n"):
    a, b = line.split(" -> ")

    x1, y1 = [int(x) for x in a.split(",")]
    x2, y2 = [int(x) for x in b.split(",")]

    x_range = full_range(x1, x2)
    y_range = full_range(y1, y2)

    if len(x_range) > len(y_range):
        for (x, y) in zip(x_range, itertools.cycle(y_range)):
            coords[x, y] += 1
    else:
        for (x, y) in zip(itertools.cycle(x_range), y_range):
            coords[x, y] += 1

print("Part 2:", len([y for y in coords.values() if y > 1]))
