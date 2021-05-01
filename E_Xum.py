n = int(input())
need = set([n-1, n+1, 2*n-1, 2*n+1])
blackboard = set([n, 2*n])
news = [n ^ 2*n]
ans = [[2*n, '+', 2*n]]


def solve():
    while True:
        for new in news:
            for black in blackboard:

                a = new ^ black
                need.add(a-1)
                need.add(a+1)
                news.append(a)
                ans.append([new, '^', black])

                b = new + black
                need.add(b-1)
                need.add(b+1)
                news.append(b)
                ans.append([new, '+', black])

            blackboard.add(new)
            if new in need:
                return


solve()

print(len(ans))
for an in ans:
    print(str(an[0]) + an[1] + str(an[0]))
