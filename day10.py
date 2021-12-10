INPUT = open('10.input').read()

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
        if stack and c == stack[-1]:
            stack.pop()
        elif c in open_to_close.keys():
            stack.append(open_to_close[c])
        else:
            raise BadLetter(c)
    return stack


answer1 = 0
answers = []

for line in INPUT.split("\n"):
    try:
        line_score = 0
        for c in reversed(scan(line)):
            line_score *= 5
            line_score += points2[c]
        answers.append(line_score)
    except BadLetter as e:
        answer1 += points[str(e)]

print("Part 1:", answer1)

ls = list(sorted(answers))

print("Part 2:", ls[len(ls) // 2])
