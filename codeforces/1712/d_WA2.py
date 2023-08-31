for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(list(zip(a, range(n))))

    for i in range(k):
        a[i] = (int(1e9), a[i][1])

    a = sorted(a, key=lambda x: x[1])
    b = [a[0][0]]
    for i in range(1, n):
        b.append(min(b[-1], a[i][0]))
    c = [a[-1][0]]
    for i in range(n-2, -1, -1):
        c.append(min(c[-1], a[i][0]))
    
    ans = 0
    for i in range(1, n):
        x, y = a[i-1][0], a[i][0]
        d = min(min(x, y), min(b[i-1]+b[i], c[i-1]+c[i]))
        ans = max(ans, d)

    print(ans)
