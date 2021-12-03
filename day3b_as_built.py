# https://adventofcode.com/2021/day/3

INPUT = [line.strip() for line in open('3.input', 'r')]

CHARS = len(INPUT[0])

most = [''] * CHARS
least = [''] * CHARS

gen_options = []
scrub_options = []

def get_common(numbers):
    for p in range(0, CHARS):
        count_1 = 0
        count_0 = 0
        for line in numbers:
            if line[p] == '1':
                count_1 += 1
            else:
                count_0 += 1
        if count_1 >= count_0:
            most[p] = '1'
            least[p] = '0'
        else:
            most[p] = '0'
            least[p] = '1'
    return most, least


for line in INPUT:
    gen_options.append(line.strip())
    scrub_options.append(line.strip())

for p in range(0, CHARS):
    if len(gen_options) > 1:
        most, least = get_common(gen_options)
        for g in list(gen_options):
            if g[p] != most[p]:
                gen_options.remove(g)

    if len(scrub_options) > 1:
        most, least = get_common(scrub_options)
        for g in list(scrub_options):
            if g[p] != least[p]:
                scrub_options.remove(g)

print(int(gen_options[0], 2) * int(scrub_options[0], 2))
