# https://adventofcode.com/2021/day/3
CHARS = 12

most = [0] * CHARS
least = [0] * CHARS

for p in range(0, CHARS):
    count_1 = 0
    count_0 = 0
    for line in open('3.input', 'r'):
        if line[p] == '1':
            count_1+=1
        else:
            count_0+=1
    if count_1 > count_0:
        most[p] = 1
        least[p] = 0
    else:
        most[p] = 0
        least[p] = 1

gamma = int(''.join([str(x) for x in most]), 2)
epislon = int(''.join([str(x) for x in least]), 2)
print(gamma, epislon)
print(gamma * epislon)

