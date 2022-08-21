def solve():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))

    x, y, z, w = 0, 1, 2, 3
    xx, yy, zz = a[0], a[1], a[2]
    while x < n-2:

        if xx == p and yy == q and zz == r:
            print("Yes")
            return
        while xx < p:
            xx += a[y]
            y += 1
        while xx > p:
            xx -= a[x]
            x += 1

        z = y + 1
        yy = a[y]
        while z < n-1 and yy + a[z] <= q:
            yy += a[z]
            z += 1
        if yy != q:
            x += 1
            continue
        
        w = z + 1
        zz = a[z]
        while w < n and zz + a[w] <= q:
            zz += a[w]
            w += 1
        
        if zz != r:
            x += 1
            continue

    print("No")
        
        
        
solve()
