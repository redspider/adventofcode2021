import itertools
import sys

INPUT = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

INPUT = open('4.input').read()

lines = INPUT.split("\n")

numbers = [int(x) for x in lines[0].split(",")]

board_n = -1
boards = []

for line in lines[1:]:
    line = line.strip()
    if line == "":
        board_n += 1
        boards.append([])
    else:
        print(boards, board_n)
        boards[board_n].append([int(x) for x in line.split(" ") if x])


def win_set(called, row):
    check = list(row)
    for n in called:
        if n in check:
            check.remove(n)

    return len(check) == 0

def is_winner(called, board):
    for row in board:
        if win_set(called, row):
            return True
    for col in zip(*board):
        if win_set(called, col):
            return True

called = []

winners = 0
count_boards = len(boards)
already_won = set()

for n in numbers:
    called.append(n)
    for i, board in enumerate(boards):
        if is_winner(called, board) and i not in already_won:
            winners += 1
            already_won.add(i)
            if count_boards == winners:
                winning_n = called[-1]
                win_sum = 0
                for row in board:
                    for x in row:
                        if x not in called:
                            win_sum += x
                print("Called is ", called)
                print("Winner is ", board)
                print("Winning n", winning_n)
                print("Winning sum", win_sum)
                print("Multiple", win_sum * winning_n)
                sys.exit(0)