import sys

INPUT = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

INPUT = open('11.input').read()

grid = dict()

for y, line in enumerate(INPUT.split("\n")):

    for x, v in enumerate(line.strip()):
        grid[x, y] = int(v)

WIDTH = max([x for x, y in grid.keys()])
HEIGHT = max([y for x, y in grid.keys()])


def print_grid(grid):
    print(f"{WIDTH}x{HEIGHT}")
    for y in range(0, HEIGHT + 1):
        line = ""
        for x in range(0, WIDTH + 1):
            line += str(grid[x, y])
        print(line)


def tick(grid):
    flashed = set()
    for p, v in grid.items():
        grid[p] += 1
    flashes = 0
    new_flashes = True
    while new_flashes:
        new_flashes = False
        for p, v in grid.items():
            if grid[p] > 9 and p not in flashed:
                flashes += 1
                new_flashes = True
                flashed.add(p)

                x, y = p

                for yo in [-1, 0, 1]:
                    for xo in [-1, 0, 1]:
                        if yo == 0 and xo == 0:
                            continue
                        if 0 <= (x + xo) <= WIDTH and 0 <= (y + yo) <= HEIGHT:
                            grid[x + xo, y + yo] += 1
    for p in flashed:
        grid[p] = 0
    return flashes


total_flashes = 0
i = 0
while True:
    # print_grid(grid)
    flashes = tick(grid)
    total_flashes += flashes
    print(f"{i} {flashes} {total_flashes}")
    i += 1
    if all(v == 0 for v in grid.values()):
        print(i)
        sys.exit(0)
