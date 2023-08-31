import math, heapq

for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))

    pos = [-1] * n
    vis = [0] * n
    rng = []

    for i, v in enumerate(p):
        cur = i+1
        l = math.ceil((cur+1) / (v+1))
        r = n if v == 0 else math.floor(cur / v)

        if l == r:
            pos[i] = l-1
            vis[l-1] = 1
        else:
            rng.append((l-1, r-1, i))
        
    if len(rng) != 0:
        rng = sorted(rng)
        
        q = []
        now = 0
        for i in range(n):
            if vis[i] == 1:
                continue
            while now < len(rng) and rng[now][0] <= i :
                heapq.heappush(q, (rng[now][1], rng[now][0], rng[now][2]))
                now += 1
            cur = heapq.heappop(q)
            pos[cur[2]] = i
            vis[i] = 1


    print(' '.join(map(lambda x: str(x+1), pos)))
