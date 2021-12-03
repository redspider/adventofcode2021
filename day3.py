# https://adventofcode.com/2021/day/3

# Part 1

grid = [list(map(int, line.strip()[::-1])) for line in open('3.input')]
gamma = sum([2**i for i, column in enumerate(zip(*grid)) if sum(column) >= (len(grid) // 2)])

print("Part 1:", gamma * (gamma ^ ((1 << gamma.bit_length()) - 1)))

# Part 2

root = [None, None, 0, 0]

for line in grid:
    node = root
    for v in line[::-1][:-1]:
        if not node[v]:
            node[v] = [None, None, 0, 0]
        node[v+2] += 1
        node = node[v]
    node[line[0]+2] += 1


def step(op, node):
    if not node:
        return ''
    if node[2] and (not node[3] or op(node[2], node[3])):
        return '0' + step(op, node[0])
    return '1' + step(op, node[1])


print("Part 2:", int(step(int.__gt__, root), 2) * int(step(int.__le__, root), 2))

# Commentary
#
# Part 1
#
# This solution uses zip to take all the rows and turn them into columns, it then
# sums the values in each column (1s and 0s) and if the sum is greater than half
# the height then there are more 1s than 0s.
#
# It converts to binary by making a >= column result 2**the column number, then summing
# all those.
#
# Finally the epsilon is always the binary inverse of the gamma. Unfortunately we can't
# use ~ because our ints are signed, but we can ^ against 0b111111...(width of row) to
# get the inverse.
#
# Part 2
#
# This solution observes that we can get the solution by traversing a binary tree constructed with the popularity of
# each node. It constructs the tree from the input then generates a path down the tree using a comparison operator
# to decide which branch to take.
#
