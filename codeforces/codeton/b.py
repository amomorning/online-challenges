for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    mn, mx = a[0], a[0]

    tot = 0
    for r in range(1, n):
        mn = min(mn, a[r])
        mx = max(mx, a[r])
        if mx - mn > x * 2:
            mx = a[r]
            mn = a[r]
            tot += 1
            
    print(tot)

