n = int(input())
sss = [0 for _ in range(100001)]
mv = 0
for a in map(int, input().split()):
    mv = max(mv, a)
    sss[a] += a

a = b  = 0
for i in range(1, mv+1):
    a, b = b + sss[i], max(a, b)

print(max(a, b))
