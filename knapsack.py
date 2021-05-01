def knapsack(w, v, N, C):
    previous = {}

    def solve(n, c):
        key = f'{n}{c}'

        if key in previous:
            return previous[key]

        if n == 0 or c == 0:
            result = 0

        elif w[n-1] > c:
            result = solve(n-1, c)

        else:
            temp1 = solve(n-1, c)
            temp2 = v[n-1] + solve(n-1, c - w[n-1])
            result = max(temp1, temp2)

        previous[key] = result

        return result

    return solve(N, C)


print(knapsack([10, 20, 30], [60, 100, 120], 3, 50))
