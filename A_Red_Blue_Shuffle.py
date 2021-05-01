
for i in range(int(input())):
    n = int(input())

    rr = [int(r) for r in input()]
    bb = [int(b) for b in input()]

    if sum(rr) / len(rr) == sum(bb) / len(bb):
        print('EQUAL')
    else:
        print('RED' if sum(rr) / len(rr) > sum(bb) / len(bb) else 'BLUE')
