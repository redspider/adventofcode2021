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

# INPUT = "[[[[<[{[(<{{{({}<>)((){})}((()())[()()])}}><[([((){})]<[()[]]{{}<>}>)[[{[]<>}][([]{})[{}()]]]]>)<{(<"


open_to_close = {
    '<': '>',
    '[': ']',
    '{': '}',
    '(': ')'
}

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

points2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


class BadLetter(Exception):
    pass


def scan(s):
    stack = []
    for c in s:
        if stack and c == open_to_close[stack[-1]]:
            stack.pop()
        elif c in open_to_close.keys():
            stack.append(c)
        else:
            raise BadLetter(c)
    return stack


answer1 = 0
for line in INPUT.split("\n"):
    try:
        scan(line)
    except BadLetter as e:
        answer1 += points[str(e)]

print("Part 1:", answer1)

answers = []

for line in INPUT.split("\n"):
    try:
        line_score = 0
        for c in reversed(scan(line)):
            line_score *= 5
            line_score += points2[open_to_close[c]]
        answers.append(line_score)
    except BadLetter as e:
        pass

ls = list(sorted(answers))

print("Part 2:", ls[len(ls) // 2])
