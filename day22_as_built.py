import re
from collections import namedtuple

INPUT = open('22.input').read()

Cube = namedtuple('Cube', ['x1', 'y1', 'z1', 'x2', 'y2', 'z2', 'multiplier'])


def overlap(a1, a2, b1, b2):
    left = max(a1, b1)
    right = min(a2, b2)
    if right < left:
        return None
    return left, right


assert overlap(0, 10, 0, 10) == (0, 10)
assert overlap(-10, 10, -20, 20) == (-10, 10)
assert overlap(-10, 5, 0, 10) == (0, 5)
assert overlap(0, 10, -10, 5) == (0, 5)
assert overlap(0, 10, 10, 20) == (10, 10)
assert overlap(0, 9, 10, 20) is None


def intersect(c1: Cube, c2: Cube, multiplier):
    """
    Intersect the two cubes and return the intersection with the given multiplier
    """
    r = overlap(c1.x1, c1.x2, c2.x1, c2.x2)
    if not r:
        return None
    x1, x2 = r

    r = overlap(c1.y1, c1.y2, c2.y1, c2.y2)
    if not r:
        return None
    y1, y2 = r

    r = overlap(c1.z1, c1.z2, c2.z1, c2.z2)
    if not r:
        return None
    z1, z2 = r

    return Cube(x1, y1, z1, x2, y2, z2, multiplier)


assert intersect(
    Cube(0, 0, 0, 10, 10, 10, 1),
    Cube(11, 11, 11, 20, 20, 20, 1),
    1
) is None

assert intersect(
    Cube(0, 0, 0, 10, 10, 10, 1),
    Cube(5, 5, 5, 20, 20, 20, 1),
    1
) == Cube(5, 5, 5, 10, 10, 10, 1)

assert intersect(
    Cube(0, 0, 0, 10, 10, 10, 1),
    Cube(10, 10, 10, 20, 20, 20, 1),
    1
) == Cube(10, 10, 10, 10, 10, 10, 1)

cubes = []

for line in INPUT.split("\n"):
    (op, cube_def) = line.split(" ")
    x1, x2, y1, y2, z1, z2 = map(int, re.search(r'x=([-\d]+)..([-\d]+),y=([-\d]+)..([-\d]+),z=([-\d]+)..([-\d]+)',
                                                line).groups())

    x1 = min(x1, x2)
    x2 = max(x1, x2)
    y1 = min(y1, y2)
    y2 = max(y1, y2)
    z1 = min(z1, z2)
    z2 = max(z1, z2)

    c = Cube(x1, y1, z1, x2, y2, z2, 1 if op == 'on' else -1)

    # if c.x2 < -50 or c.x1 > 50 or c.y2 < -50 or c.y1 > 50 or c.z2 < -50 or c.z1 > 50:
    #     continue

    for check_cube in list(cubes):
        # If it's a subtract then it should remove from any positives and add to any negatives
        # If it's an add it should remove from any positives and add to any negatives
        sub_cube = intersect(check_cube, c, check_cube.multiplier * -1)
        if sub_cube:
            cubes.append(sub_cube)
    if op == 'on':
        cubes.append(c)

total_volume = sum([
    (c.x2 - c.x1 + 1) * (c.y2 - c.y1 + 1) * (c.z2 - c.z1 + 1) * c.multiplier for c in cubes
])

print("Part 2:", total_volume)
