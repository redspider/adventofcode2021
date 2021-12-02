# Sonar sweep https://adventofcode.com/2021/day/1
items = [int(x) for x in open('1.input', 'r')]

print("Part 1:", sum([b > a for a, b in zip(items[:-1], items[1:])]))
print("Part 2:", sum([b > a for a, b in zip(items[:-3], items[3:])]))
