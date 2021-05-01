for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = sum(a)
    a.sort()

    if b == 0:
        print('NO')
    elif b > 0:
        print('YES')
        print(' '.join(map(str, a[::-1])))
    else :
        print('YES')
        print(' '.join(map(str, a)))
