n, m = map(int, input().split())
v = list(map(int, input().split()))
r = 0
for i in range(m):
    r += min(v[i] for i in map(int, input().split()))
    
print(r)
    