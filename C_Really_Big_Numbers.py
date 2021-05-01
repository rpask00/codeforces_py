n, s = map(int, input().split())
r = 0
v = min(n+1, s+19*9)
for i in range(s, v):
    zz = f'{i}'
    sm = i
    for z in zz:
        sm -= int(z)

    if(sm >= s):
        r += 1

print(r + n-v + 1)
