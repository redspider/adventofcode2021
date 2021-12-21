people = list(range(1, 101))

while len(people) > 1:
    people = people[2:] + [people[0]]

print("Part 1:", people)

people = list(range(1, 1547))

while len(people) > 1:
    people = people[2:] + [people[0]]

print("Part 2:", people)