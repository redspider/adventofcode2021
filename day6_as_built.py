from functools import cache

#INPUT = """3,4,3,1,2"""
INPUT = open('6.input').read()

days = 256


@cache
def spawn_fish(days_left, timer):
    count = 1
    while True:
        days_left -= timer+1
        if days_left < 0:
            break
        timer = 6
        count += spawn_fish(days_left, 8)
    return count


total = 0
for timer in [int(x) for x in INPUT.split(",")]:
    total += spawn_fish(days, timer)

print(total)