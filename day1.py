# Sonar sweep https://adventofcode.com/2021/day/1
items = [int(x) for x in open('1.input', 'r')]

print("Part 1:", sum([b > a for a, b in zip(items[:-1], items[1:])]))
print("Part 2:", sum([b > a for a, b in zip(items[:-3], items[3:])]))

# Commentary
# The solutions above work on the observation that you could solve it by comparing the same list against itself
# shifted. Part 1 works by simply comparing the values from index 0...length-1 with 1...length.
#
# Part 2 is exactly the same, but compares the values from 0...length-3 with 3...length. This works because if we have
# four numbers in our list:
#
# 1,2,3,4
#
# and we compare the sum of
#
# 1,2,3 with 2,3,4
#
# the 2 and 3 cancel out on both sides, so we really just care whether 4 is bigger than 1.
