for t in range(int(input())):
    n, W = map(int, input().split())
    ans = ''
    w = list(map(int, input().split()))

    stack = [(0, 0)]
    for i, ww in enumerate(w):
        for j in range(len(stack)):
            sw, si = stack[j]
            if sw + ww <= W:
                stack.append((sw + ww, si | 1 << i))
                if sw + ww >= W/2 :
                    ans = str(bin(si | 1 << i))[2:]
                    break
        else:
            continue

        break

    aaaa = []
    for i, a in enumerate(reversed(ans)):
        if int(a):
            aaaa.append(str(i+1))

    print(len(aaaa) if len(aaaa) else -1)
    if len(aaaa):
        print(' '.join(aaaa))
