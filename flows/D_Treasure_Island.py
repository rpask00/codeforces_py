n, m = map(int, input().split())
right = [0 for _ in range(n*m+1)]
down = [0 for _ in range(n*m+1)]
vis = [0 for _ in range(n*m+1)]

# g = Graph()


def solve():
    index = 1
    for i in range(n):
        ss = input()
        # ss = '.'
        for j in range(m):
            if ss[j] == '#':
                if n == 1 or m == 1:
                    return 0

                index += 1
                continue

            if j:
                right[index-1] = index

            if i:
                down[index - m] = index

            index += 1


    if n == 1 or m == 1:
        return 1

    res = 0
    for i in range(2):
        path = []
        node = 1
        vis[n*m] = 0
        while node != n*m:
            if down[node] and not vis[down[node]]:
                vis[down[node]] = 1
                path.append(node)
                node = down[node]

            elif right[node] and not vis[right[node]]:
                vis[right[node]] = 1
                path.append(node)
                node = right[node]

            elif path:
                node = path.pop()
            else:
                break
        else:
            res += 1

    
    return res

print(solve())