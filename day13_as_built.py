INPUT = open('13.input').read()

grid = set()

read_folds = False

folds = []

for line in INPUT.split("\n"):
    if not line.strip():
        read_folds = True
        continue

    if read_folds:
        line = line.replace('fold along ', '')
        axis, v = line.split('=')
        folds.append((axis, int(v)))
    else:
        x, y = [int(n) for n in line.split(',')]
        grid.add((x, y))


def fold(grid, axis, v):
    output = set()
    if axis == 'y':
        for x, y in grid:
            if y < v:
                output.add((x, y))
            else:
                output.add((x, v - (y - v)))
    else:
        for x, y in grid:
            if x < v:
                output.add((x, y))
            else:
                output.add((v - (x - v), y))
    return output


def print_grid(grid):
    w = max([x for x, y in grid])
    h = max([y for x, y in grid])
    for y in range(0, h + 1):
        line = ""
        for x in range(0, w + 1):
            if (x, y) in grid:
                line += '#'
            else:
                line += ' '
        print(line)
    print("\n")


output = set(grid)

for axis, v in folds[:1]:
    output = set(fold(output, axis, v))

print("Part 1:", len(output))

for axis, v in folds:
    output = set(fold(output, axis, v))

print("Part 2:")
print_grid(output)
