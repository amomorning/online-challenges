for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    divs = []
    divs.append(a[0] + n - a[-1] - 1)
    for i in range(1, m):
        divs.append(a[i] - a[i-1] - 1)

    divs = sorted(divs, reverse=True)
    # print(divs)
    cur = 1
    for i in range(0, m):
        if cur < divs[i]:
            divs[i] = cur
        elif cur == divs[i]:
            divs[i] -= 1
        cur += 4
        
    # print(divs)
    print(sum(divs) + m)
