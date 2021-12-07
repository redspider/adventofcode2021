INPUT = """16,1,2,0,4,2,7,1,2,14"""

positions = [int(x) for x in INPUT.split(",")]

print("Part 1:", min([sum([abs(p - c) for p in positions]) for c in range(min(positions), max(positions))]))
print("Part 2:", min([sum([(abs(p - c)*(abs(p - c)+1))//2 for p in positions]) for c in range(min(positions), max(positions))]))
