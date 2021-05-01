
def calculate(game):
    if not game:
        return 0
    su = 1 if game[0] == 'W' else 0
    prev = game[0]

    for g in game[1:]:
        if g == 'W':
            su += 2 if prev == 'W' else 1
            prev = 'W'
        else:
            prev = 'L'

    return su


for t in range(int(input())):
    n, k = map(int, input().split())
    games = input()
    gaps = list(map(len, games.split(('W'))))
    front_end = []
    bonus = 0

    if len(gaps):
        front_end.append(gaps.pop(0))

    if len(gaps):
        front_end.append(gaps.pop())
    else:
        bonus = -1 if k else 0

    front_end = [f for f in front_end if f]
    front_end.sort()
    gaps = [g for g in gaps if g]
    gaps.sort()

    while k:
        if gaps:
            top = gaps.pop(0)
            midgap = 1
        elif front_end:
            top = front_end.pop(0)
            midgap = 0
        else:
            break

        if top > k:
            bonus += k*2
            k = 0
        else:
            bonus += top*2 + midgap
            k -= top


    print(calculate(games) + bonus)
