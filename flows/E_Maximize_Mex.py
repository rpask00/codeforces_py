n, m = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
d = int(input())
k = []
for i in range(d):
    k.append(int(input()))
 
vis = [False for i in range(m+1)]
match = [-1 for i in range(m+1)]
 
 
def dfs(u: int) -> bool:
    for club in edges[u]:
        if not vis[club]:
            vis[club] = True
            if match[club] == -1 or dfs(match[club]):
                match[club] = u
                return True
    return False
 
 
edges = [[] for i in range(5005)]
for i in range(n):
    if i + 1 not in k:
        edges[p[i]].append(c[i])
 
mex = 0
ans = []
for i in range(d - 1, -1, -1):
    while True:
        vis = [False for j in range(m+1)]
        if not dfs(mex):
            break
        mex += 1
    ans.append(mex)
    edges[p[k[i]-1]].append(c[k[i]-1])
 
for i in reversed(ans):
    print(i)