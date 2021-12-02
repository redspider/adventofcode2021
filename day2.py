# Dive! https://adventofcode.com/2021/day/2
commands = [(c, int(v)) for c, v in [line.split(' ') for line in open('2.input', 'r')]]

# Part 1
position = 0
depth = 0

for command, value in commands:
    if command == 'forward':
        position += value
    elif command == 'down':
        depth += value
    elif command == 'up':
        depth -= value

print("Part 1:", position * depth)

# Part 2
position = 0
depth = 0
aim = 0

for command, value in commands:
    if command == 'forward':
        position += value
        depth += aim * value
    elif command == 'down':
        aim += value
    elif command == 'up':
        aim -= value

print("Part 2:", position * depth)


# Commentary
# I should read the instructions more carefully lol.
# Nothing tricky with this one.
