from collections import Counter, defaultdict
from functools import cache

INPUT = open('14.input').read()

lines = INPUT.split("\n")
template = lines[0].strip()
rules = dict()
for line in lines[2:]:
    r, o = line.split(" -> ")
    rules[(r[0], r[1])] = o


def apply_rules(polymer):
    output = ""
    for a, b in zip(polymer[:-1], polymer[1:]):
        output += a + rules.get((a, b), '')
    return output + polymer[-1]


pairs = defaultdict(int)
for a, b in zip(template[:-1], template[1:]):
    pairs[a, b] += 1

output = template
for step in range(0, 15):
    output = apply_rules(output)
    c = Counter(output)

c = Counter(output)
print("Part 1:", max(c.values()) - min(c.values()))


@cache
def count_insert(a, b, depth):
    counter = defaultdict(int)
    if depth == 0:
        return counter
    if (a, b) not in rules:
        return counter

    c = rules[a, b]
    for k, v in count_insert(a, c, depth - 1).items():
        counter[k] += v
    for k, v in count_insert(c, b, depth - 1).items():
        counter[k] += v
    counter[c] += 1

    return counter


counter = defaultdict(int)
for a, b in zip(template[:-1], template[1:]):
    for k, v in count_insert(a, b, 40).items():
        counter[k] += v
    counter[a] += 1

counter[template[-1]] += 1
print("Part 2:", max(counter.values()) - min(counter.values()))
