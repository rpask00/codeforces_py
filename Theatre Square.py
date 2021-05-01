for t in range(int(input())):
    square = []
    cost = 0
    n, m, x, y = map(int, input().split())

    for i in range(n):
        square.append(input())

    is_worth = x*2 > y

    for s in square:
        if is_worth:
            cost += s.count('..')*y
            s = ''.join(s.split('..'))
            cost += s.count('.')*x
        else:
            cost += s.count('.')*x
    print(cost)
