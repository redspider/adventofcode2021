def solve(n):
    people = list(range(1, n + 1))

    while len(people) > 1:
        people = people[2:] + [people[0]]

    return people[0]


def solve2(n):
    return (n - 2 ** (n.bit_length() - 1)) * 2 + 1


for n in range(2, 100):
    print(n, solve(n), solve2(n))

print(solve2(1496))

print(solve2(30_000_000_000))
