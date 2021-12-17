import re


class BoundingBox(object):
    x1: int
    y1: int
    x2: int
    y2: int

    def __init__(self, x1, x2, y1, y2):
        self.x1 = min(x1, x2)
        self.y1 = min(y1, y2)
        self.x2 = max(x1, x2)
        self.y2 = max(y1, y2)

    def contains(self, x, y):
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2

    def is_past(self, x, y):
        return x > self.x2 or y < self.y1

    def __str__(self):
        return f"Target({self.x1}, {self.y1}, {self.x2}, {self.y2})"


class Probe(object):
    x: int
    y: int
    xv: int
    yv: int

    def __init__(self, xv: int, yv: int):
        self.x = 0
        self.y = 0
        self.xv = xv
        self.yv = yv

    def step(self):
        self.x += self.xv
        self.y += self.yv

        if self.xv > 0:
            self.xv -= 1
        elif self.xv < 0:
            self.xv += 1

        self.yv -= 1


INPUT = "target area: x=20..30, y=-10..-5"

target = BoundingBox(*map(int, re.search(r'x=([-\d]+)..([-\d]+), y=([-\d]+)..([-\d]+)', INPUT).groups()))

print(target)

max_y = -1000

for yv in range(-160, 200):
    for xv in range(1, target.x2+1):
        p = Probe(xv, yv)
        ys = []
        while not target.is_past(p.x, p.y):
            ys.append(p.y)
            p.step()
            if target.contains(p.x, p.y):
                max_y = max(max_y, *ys)

print("Part 1:", max_y)

options = set()

for yv in range(-160, 200):
    for xv in range(1, target.x2+1):
        p = Probe(xv, yv)
        ys = []
        while not target.is_past(p.x, p.y):
            ys.append(p.y)
            p.step()
            if target.contains(p.x, p.y):
                options.add((xv, yv))

print("Part 2:", len(options))
