n = int(input())
f =  list(map(int, input().split()))

print('NO' if all([f[f[f[x-1]-1]-1] != x for x in f]) else "YES")
