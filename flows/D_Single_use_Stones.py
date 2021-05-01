w, l = map(int, input().split())
a = list(map(int, input().split()))


x = y = sum(a[:l])

for i in range(w-l-1):
    y = y - a[i] + a[i+l]
    x = min(y,x)

print(x)
