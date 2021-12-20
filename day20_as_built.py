## WARNING: This doesn't work, I never completed it due to the logic trick totally demotivating me heh


# INPUT = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#
#
# #..#.
# #....
# ##..#
# ..#..
# ..###"""

image = set()

INPUT = open('20.input').read()

E = INPUT.split("\n")[0]

print(len(E))

for y, line in enumerate(INPUT.split("\n")[2:]):
    if line:
        for x,pixel in enumerate(line):
            if pixel == '#':
                image.add((x,y))

def print_grid(grid):
    sx =  min([x for x, y in grid])
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
    right = max(x for x,y in image)
    top = min(y for x, y in image)
    bottom = max(y for x,y in image)

    for x in range(left-1, right+2):
        for y in range(top-1, bottom/+2):
            b = ""
            for yo in range(-1, 2):
                for xo in range(-1, 2):
                    if xo < left or xo > right or yo < top or yo > bottom:
                        b += outside
                    else:
                        if (x+xo, y+yo) in image:
                            b += '1'
                        else:
                            b += '0'
            n = int(b, 2)
            if E[n] == '#':
                output.add((x, y))
    return output


o = set(image)
for i in range(0, 2):
    print(f"{i} {len(o)} {min([x for x,y in o])} {min([y for x,y in o])} {max([x for x,y in o])} {max([y for x,y in o])}")
    #print_grid(o)
    o = enhance(o, outside = ('0' if i % 2 else '1'))

print_grid(o)

print(f"{i} {len(o)} {min([x for x,y in o])} {min([y for x,y in o])} {max([x for x,y in o])} {max([y for x,y in o])}")
print(f"Final {len(o)}")
