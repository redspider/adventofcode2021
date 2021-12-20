## WARNING: This doesn't work, I never completed it due to the logic trick totally demotivating me heh


# INPUT = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#
#
# #..#.
# #....
# ##..#
# ..#..
# ..###"""
import matplotlib.pyplot as plt
import numpy as np

image = set()

INPUT = open('20.input').read()

E = INPUT.split("\n")[0]

print(len(E))

for y, line in enumerate(INPUT.split("\n")[2:]):
    line = line.strip()
    if line:
        for x, pixel in enumerate(line):
            if pixel == '#':
                image.add((x, y))


def draw_grid(grid, width=None, height=None):
    """
    Draws a provided grid into sciview, with a minimum of width/height

    :param grid: set of points
    :param width: minimum width
    :param height: minimum height
    """
    x1 = min([x for x, y in grid])
    y1 = min([y for x, y in grid])
    x2 = max([x for x, y in grid])
    y2 = max([y for x, y in grid])

    if width and width > x2 - x1:
        x1 = (x2 + x1) // 2 - width // 2
        x2 = x1 + width

    if height and height > y2 - y1:
        y1 = (y2 + y1) // 2 - height // 2
        y2 = y1 + height

    data = []
    for y in range(y1, y2 + 1):
        row = []
        for x in range(x1, x2 + 1):
            if (x, y) in grid:
                row.append(1)
            else:
                row.append(0)
        data.append(row)

    d = np.array(data)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()
    ax.imshow(d, cmap='binary', interpolation='nearest')
    plt.show()


def print_grid(grid):
    sx = min([x for x, y in grid])
    sy = min([y for x, y in grid])
    w = max([x for x, y in grid])
    h = max([y for x, y in grid])
    for y in range(sy, h + 1):
        line = ""
        for x in range(sx, w + 1):
            if (x, y) in grid:
                line += '#'
            else:
                line += ' '
        print(line)
    print("\n")


def enhance(image, outside):
    output = set()

    left = min(x for x, y in image)
    right = max(x for x, y in image)
    top = min(y for x, y in image)
    bottom = max(y for x, y in image)

    for x in range(left - 1, right + 2):
        for y in range(top - 1, bottom + 2):
            b = ""
            for yo in range(y - 1, y + 2):
                for xo in range(x - 1, x + 2):
                    if xo < left or xo > right or yo < top or yo > bottom:
                        b += outside
                    else:
                        if (xo, yo) in image:
                            b += '1'
                        else:
                            b += '0'
            n = int(b, 2)
            if E[n] == '#':
                output.add((x, y))
    return output


o = set(image)
for i in range(0, 2):
    print(
        f"{i} {len(o)} {min([x for x, y in o])} {min([y for x, y in o])} {max([x for x, y in o])} {max([y for x, y in o])}")
    draw_grid(o, 200, 200)
    o = enhance(o, outside=('0' if i % 2 == 0 else '1'))

draw_grid(o, 200, 200)

print(
    f"{i} {len(o)} {min([x for x, y in o])} {min([y for x, y in o])} {max([x for x, y in o])} {max([y for x, y in o])}")
print(f"Final {len(o)}")
