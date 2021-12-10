INPUT = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

INPUT = open('10.input').read()

#INPUT = "[[[[<[{[(<{{{({}<>)((){})}((()())[()()])}}><[([((){})]<[()[]]{{}<>}>)[[{[]<>}][([]{})[{}()]]]]>)<{(<"

class BadLetter(Exception):
    pass

open_to_close = {
    '<': '>',
    '[': ']',
    '{': '}',
    '(': ')'
}

points={
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def consume(s):
    if len(s) == 1:
        return ''
    letter = s[0]

    if s[1] == open_to_close[letter]:
        return s[2:]
    remainder = s[1:]

    while remainder[0] in open_to_close.keys():
        remainder = consume(remainder)
        if not remainder:
            return ''

    if remainder[0] != open_to_close[letter]:
        # print(f"Expected {open_to_close[letter]} but found {remainder[0]} instead")
        raise BadLetter(remainder[0])

    return remainder[1:]


class Foo(object):
    extra: str

    def __init__(self):
        self.extra = ''

    def full_fix(self, s):
        while s:
            s = self.fix(s)

    def fix(self, s):
        if not s:
            return ''
        if len(s) == 1:
            self.extra += open_to_close[s]
            return ''
        letter = s[0]

        if s[1] == open_to_close[letter]:
            return s[2:]
        remainder = s[1:]
        while remainder[0] in open_to_close.keys():
            remainder = self.fix(remainder)
            if not remainder:
                self.extra += open_to_close[letter]
                return ''

        return remainder[1:]




answer1 = 0
for line in INPUT.split("\n"):
    try:
        consume(line)
    except BadLetter as e:
        answer1 += points[str(e)]

print("Part 1:", answer1)


clean_lines = []

for line in INPUT.split("\n"):
    try:
        consume(line)
        clean_lines.append(line)
    except BadLetter as e:
        pass

# clean_lines = ['[(()[<>])]({[<{<<[]>>(']

answer2 = 0

points2 = {
    ')':1,
    ']': 2,
    '}': 3,
    '>': 4
}

answers = []

for line in clean_lines:
    f = Foo()
    f.full_fix(line)
    line_score = 0
    if f.extra:
        for c in f.extra:
            line_score *= 5
            line_score += points2[c]
        answers.append(line_score)

ls = list(sorted(answers))

print("Part 2:", ls[len(ls) // 2])