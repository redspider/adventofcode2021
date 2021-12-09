import functools
from collections import defaultdict

INPUT = open('9.input').read()

f = lambda: 2**32

grid = defaultdict(f)

for y, line in enumerate(INPUT.split("\n")):
    for x, p in enumerate(line):
        grid[x, y] = int(p)

WIDTH = max(x for x, y in grid.keys())
HEIGHT = max(y for x, y in grid.keys())

total_risk = 0

low_points = []

for x, y in list(grid.keys()):
    v = grid[x, y]
    if grid[x - 1, y] > v and grid[x + 1, y] > v and grid[x, y - 1] > v and grid[x, y + 1] > v:
        low_points.append((x, y, v))
        total_risk += 1 + v

print("Part 1:", total_risk)


# Use recursive solution from x, y for each low point to size the basin
# expand recursively until edges or 9s

def count_from(grid, counted, x, y):
    if (x, y) in counted:
        return 0

    if grid[x, y] == 9:
        return 0

    counted.add((x, y))
    size = 1

    if x > 0:
        size += count_from(grid, counted, x - 1, y)
    if x < WIDTH:
        size += count_from(grid, counted, x + 1, y)
    if y > 0:
        size += count_from(grid, counted, x, y - 1)
    if y < HEIGHT:
        size += count_from(grid, counted, x, y + 1)

    return size


basin_sizes = []

for cx, cy, cv in low_points:
    counted = set()
    basin_sizes.append(count_from(grid, counted, cx, cy))

print("Part 2:", functools.reduce(int.__mul__, sorted(basin_sizes)[-3:]))
