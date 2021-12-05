from collections import defaultdict

INPUT = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

#INPUT = "3,3 -> 1,1"

INPUT = open('5.input').read()

coords = defaultdict(int)

for line in INPUT.split("\n"):
    a, b = line.split(" -> ")
    x1, y1 = [int(x) for x in a.split(",")]
    x2, y2 = [int(x) for x in b.split(",")]

    if x1 == x2 and y1 != y2:
        if y1 > y2:
            y2, y1 = y1, y2
        for y in range(y1, y2 + 1):
            coords[(x1, y)] += 1
    elif y1 == y2 and x1 != x2:
        if x1 > x2:
            x2, x1 = x1, x2

        for x in range(x1, x2 + 1):
            coords[(x, y1)] += 1
    else:
        x_step = 1
        if x1 > x2:
            x_step = -1
        y_step = 1

        if y1 > y2:
            y_step = -1

        for i in range(0, abs(x1 - x2)+ 1):
            x = x1 + x_step * i
            y = y1 + y_step * i
            coords[(x, y)] += 1
print("Part 2:", len([x for x in coords.values() if x > 1]))
