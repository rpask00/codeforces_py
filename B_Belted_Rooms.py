for t in range(int(input())):
    l = set()
    n = int(input())
    d = ''
    a = True
    for i, b in enumerate(input()):
        if b == '-':
            l.add((i+1) % n)
            l.add(i)
            continue

        if not d:
            d = b

        if b != d:
            a = False

    print(n if a else len(l))
