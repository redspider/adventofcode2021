import itertools

INPUT = open('4.input').read()

lines = INPUT.split("\n")

numbers = [int(x) for x in lines[0].split(",")]

boards = []
for line in lines[1:]:
    line = line.strip()
    if not line:
        boards.append([])
    else:
        boards[-1].append([int(x) for x in line.split(" ") if x])


def is_winner(called, board):
    return any([set(row).issubset(called) for row in board] + [set(col).issubset(called) for col in zip(*board)])


called = []
winners = set()

for n in numbers:
    called.append(n)
    for i, board in enumerate(boards):
        if i not in winners and is_winner(called, board):
            winners.add(i)
            winning_sum = sum(set(itertools.chain(*board)).difference(set(called)))

            if len(winners) == 1:
                print("Part 1", called[-1] * winning_sum)

            if len(winners) == len(boards):
                print("Part 2", called[-1] * winning_sum)

# Commentary
#
# Two fun pieces here. The first is the win condition check—full match in any row or column. We already know how to
# create columns from rows using zip(*rows), the is_winner function just builds on this with set()s to check whether
# the row (or column) is a full subset of the called numbers so far. We use any() to return true if any of them are
# full subsets.
#
# The second piece is calculating the sum of all uncalled numbers on the board. We use itertools.chain(*board) to
# "flatten" the rows into a single list, then we use set.difference() to get the subset that aren't matched and sum
# them.
#
