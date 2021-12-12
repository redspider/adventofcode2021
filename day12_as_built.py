import networkx as nx

INPUT = open('12.input').read()

G = nx.Graph()

all_nodes = set()

for line in INPUT.split("\n"):
    (f, t) = line.split('-')
    G.add_edge(f, t)
    all_nodes.add(f)
    all_nodes.add(t)

low_nodes = set([n for n in all_nodes if n.islower() and n not in ['start', 'end']])


def find_path(G, path, counter):
    if path[-1] == 'end':
        found.add('-'.join(path))
        return

    for edge in G[path[-1]]:
        nc = dict(counter)
        if edge == 'start':
            continue
        if edge in low_nodes:
            if nc[edge] > 0:
                nc[edge] -= 1
                find_path(G, path + [edge], nc)
            continue
        find_path(G, path + [edge], nc)


def make_counter():
    counter = dict()
    for e in low_nodes:
        if e in low_nodes:
            counter[e] = 1
    return counter


found = set()

for n in low_nodes:
    c = make_counter()
    find_path(G, ['start'], c)

print("Part 1:", len(found))


found = set()

for n in low_nodes:
    c = make_counter()
    c[n] = 2
    find_path(G, ['start'], c)

print("Part 2:", len(found))
