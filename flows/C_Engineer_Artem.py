q = int(input())

for i in range(q):
    mtr = []
    n, m = map(int, input().split())
    for i in range(n):
        mtr.append(list(map(int, input().split())))

    offset = 0
    for i in range(n):
        offset = (offset + 1) % 2
        for j in range(offset, m, 2):
            mtr[i][j] = mtr[i][j] if mtr[i][j] % 2 == 1 else mtr[i][j]+1

        for j in range((offset + 1) % 2, m, 2):
            mtr[i][j] = mtr[i][j] if mtr[i][j] % 2 == 0 else mtr[i][j]+1

    for i in range(n):
        for j in range(m):
            print(mtr[i][j] ,end=' ')
        print('')