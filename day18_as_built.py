import itertools

INPUT = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""

INPUT = open('18.input').read()

triggered = False


def do_add(a, b):
    return [a, b]


def do_explode_decode(v, instructions, depth=0):
    global triggered
    if isinstance(v, list):
        if depth < 4 or triggered:
            instructions.append(('nest', None))
            do_explode_decode(v[0], instructions, depth + 1)
            do_explode_decode(v[1], instructions, depth + 1)
            instructions.append(('unnest', None))
            return
        else:
            triggered = True
            instructions.append(('add_above', v[0]))
            instructions.append(('item', 0))
            instructions.append(('add_below', v[1]))
            return
    else:
        instructions.append(('item', v))
        return


def do_explode(l):
    global triggered
    instructions = []
    do_explode_decode(l, instructions, 0)

    last_item_index = None
    carry = 0

    # explode
    output = []
    for op, v in instructions:
        if op == 'item':
            output.append([op, v + carry])
            carry = 0
            last_item_index = len(output) - 1
        elif op == 'add_above':
            if last_item_index is not None:
                output[last_item_index][1] += v
        elif op == 'add_below':
            carry = v
        else:
            output.append([op, v])

    # transform
    stack = [[]]

    for op, v in output:
        if op == 'nest':
            stack.append([])
        elif op == 'unnest':
            stack[-2].append(stack[-1])
            stack.pop()
        elif op == 'item':
            stack[-1].append(v)

    return stack[0]


def do_split(l):
    global triggered
    output = []
    for v in l:
        if isinstance(v, list):
            output.append(do_split(v))
        else:
            if v >= 10 and not triggered:
                triggered = True
                output.append([v // 2, v - v // 2])
            else:
                output.append(v)
    return output


def do_reduce(l):
    global triggered
    triggered = True
    while triggered:
        triggered = False
        l = do_explode(l)
        l = do_split(l)[0]
    return l


def cm(a, b):
    if isinstance(a, list):
        a = cm(*a)
    if isinstance(b, list):
        b = cm(*b)
    return 3 * a + 2 * b


def calc_magnitude(l):
    return cm(l[0], l[1])


current = None

for line in INPUT.split("\n"):
    l = eval(line)
    if not current:
        current = l
    else:
        current = do_reduce(do_add(current, l))

print("Part 1:", calc_magnitude(current))

max_output = 0

sns = [eval(line) for line in INPUT.split("\n")]

for a, b in itertools.permutations(sns, 2):
    max_output = max(max_output, calc_magnitude(do_reduce(do_add(a, b))))

print("Part 2:", max_output)
