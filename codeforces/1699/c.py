
mod = int(1e9+7)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if n < 2:
        print(1)
        continue

    p = [0] * n
    for i in range(n):
        p[a[i]] = i
    
    l, r = p[0], p[1]
    if l > r: l, r = r, l

    tot = 1
    for i in range(2, n):
        if l < p[i] and p[i] < r:
            tot = tot * (r-l-i+1) % mod
        elif p[i] < l:
            l = p[i]
        elif p[i] > r:
            r = p[i]
    print(tot)

    
