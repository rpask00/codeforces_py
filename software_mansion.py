def calculate(A, B, n):
    counts = [0] * (n + 1)

    for b in B:
        counts[b] += 1

    is_prime = [False, False] + [True] * (n - 1)

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    return [a for a in A if not is_prime[counts[a]]]


_n = 10000

_A = [2, 3, 9, 2, 5, 1, 3, 7, 10]
_B = [2, 1, 3, 4, 3, 10, 6, 6, 1, 7, 10, 10, 10]

C = calculate(_A, _B, _n)

# [2, 9, 2, 5, 7, 10]
print(C)

# Złożoność obliczeniowa algorytmu to O(n * log log (n)),
# gdyż jest to sama złożoność mechanizmu obliczania liczb pierwszych za pomocą sita Eratostenesa,
# natomisat samo zliczanie wystąpień tablicy odbywa się w czasie liniowym O(n),
# więc nie wpływa ono na finalną złożoność algorithmu.
