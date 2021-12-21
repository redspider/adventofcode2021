from functools import cache


class Player(object):
    score: int
    position: int

    def __init__(self, starting_position: int):
        self.score = 0
        self.position = starting_position

    def move(self, amount):
        self.position = (self.position -1 + amount) % 10 + 1
        self.score += self.position

test_player = Player(7)
test_player.move(5)
assert test_player.position == 2
assert test_player.score == 2

players = [Player(7), Player(1)]


dice = 0
while (all(p.score < 1000 for p in players)):
    for p in players:
        dice += 1
        move_distance = dice + dice+1 + dice+2
        dice += 2
        p.move(move_distance)
        if p.score >= 1000:
            break


@cache
def count_wins(p1_position, p2_position, p1_score, p2_score, turn):
    wins = [0,0]

    players = [Player(p1_position), Player(p2_position)]
    players[0].score = p1_score
    players[1].score = p2_score

    for r1 in range(1, 4):
        for r2 in range(1, 4):
            for r3 in range(1, 4):
                p = players[turn]
                old_position = p.position
                old_score = p.score
                p.move(r1+r2+r3)
                if p.score >= 21:
                    wins[turn] += 1
                else:
                    if turn == 0:
                        for i, v in enumerate(count_wins(p.position, p2_position, p.score, p2_score, 1)):
                            wins[i] += v
                    else:
                        for i, v in enumerate(count_wins(p1_position, p.position, p1_score, p.score, 0)):
                            wins[i] += v
                p.position = old_position
                p.score = old_score
    return wins




print("Part 1:", [p.score for p in players], dice, min(p.score for p in players) * dice)

print("Part 2:", max(count_wins(7, 1, 0, 0, 0)))