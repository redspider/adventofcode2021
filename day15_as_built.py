import networkx as nx

INPUT = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

INPUT = open('15.input').read()

G = nx.DiGraph()

nodes = set()
for y, line in enumerate(INPUT.split("\n")):
    for x, v in enumerate(line.strip()):
        nodes.add((x, y))

w = max([x for x, y in nodes])
h = max([y for x, y in nodes])

for y, line in enumerate(INPUT.split("\n")):
    for x, v in enumerate(line.strip()):
        v = int(v)
        if x > 0:
            G.add_edge((x - 1, y), (x, y), cost=v)
        if x < w:
            G.add_edge((x + 1, y), (x, y), cost=v)
        if y > 0:
            G.add_edge((x, y - 1), (x, y), cost=v)
        if y < h:
            G.add_edge((x, y + 1), (x, y), cost=v)

print("Part 1", nx.shortest_path_length(G, (0, 0), (w, h), 'cost'))

G = nx.DiGraph()

for yo, line in enumerate(INPUT.split("\n")):
    for xo, vo in enumerate(line.strip()):
        vo = int(vo)

        for xi in range(0, 5):
            for yi in range(0, 5):
                x = xo + (w + 1) * xi
                y = yo + (h + 1) * yi
                v = ((vo + xi + yi) - 1) % 9 + 1

                if x > 0:
                    G.add_edge((x - 1, y), (x, y), cost=v)
                if x < (w + 1) * 5 - 1:
                    G.add_edge((x + 1, y), (x, y), cost=v)
                if y > 0:
                    G.add_edge((x, y - 1), (x, y), cost=v)
                if y < (h + 1) * 5 - 1:
                    G.add_edge((x, y + 1), (x, y), cost=v)

print("Part 2", nx.shortest_path_length(G, (0, 0), ((w + 1) * 5 - 1, (h + 1) * 5 - 1), 'cost'))
