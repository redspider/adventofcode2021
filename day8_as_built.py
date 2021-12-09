import itertools
from collections import defaultdict

digits = [
    'abcefg',
    'cf',
    'acdeg',
    'acdfg',
    'bcdf',
    'abdfg',
    'abdefg',
    'acf',
    'abcdefg',
    'abcdfg',
]

dset = [set(x) for x in digits]

len_digits = {
    2: 1,
    3: 7,
    4: 4,
    7: 8
}

CHECK = 'deafgbc'

INPUT = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

INPUT = open('8.input').read()

count = defaultdict(int)

for line in INPUT.split("\n"):
    (ins, outs) = line.split(" | ")
    ins = ins.split(" ")
    outs = outs.split(" ")

    for o in outs:
        if len(o) in len_digits:
            count[len_digits[len(o)]] += 1

print("Part 1:", sum(count.values()))


def valid_mapping_vs_all(m, all):
    for code in all:
        plain = code.translate(str.maketrans(m, 'abcdefg'))
        if set(plain) not in dset:
            return False
    return True


def find_mapping(ins, outs):
    all = set(ins + outs)

    for mapping in itertools.permutations('abcdefg'):
        mapping = ''.join(list(mapping))

        if not valid_mapping_vs_all(mapping, all):
            continue

        line = ''
        for code in outs:
            plain = code.translate(str.maketrans(mapping, 'abcdefg'))
            line += str(dset.index(set(plain)))
        return line


total = 0

for line in INPUT.split("\n"):
    (ins, outs) = line.split(" | ")
    ins = ins.split(" ")
    outs = outs.split(" ")

    total += int(find_mapping(ins, outs))
print("Part 2:", total)
