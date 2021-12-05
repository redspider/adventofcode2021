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

    line_length = max(abs(x1-x2), abs(y1-y2))
    for i in range(0, line_length+1):
        coords[x1+i*(x2-x1)/line_length, y1+i*(y2-y1)/line_length] += 1

print("Part 2:", len([y for y in coords.values() if y > 1]))
