t = int(input())

paths = []

def bfs(root, a):
    global paths
    q = list()
    q.append(root)
    f, e = 0, len(q)
    nxt = {}

    while(f < e):
        u = q[f]
        f += 1

        # print(u)

        if(u not in G):
            p = [u]
            fu = a[u]-1
            if(fu not in nxt):
                paths.append(p[::-1])
                continue

            while(nxt[fu] == u):
                u = fu
                fu = a[u]-1
                p.append(u)

            paths.append(p[::-1])
            continue

        for v in G[u]:
            if(u not in nxt):
                nxt[u] = v
            q.append(v)
            e += 1

    

while(t > 0): 
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))

    G = {}
    for i in range(n):
        if(i == a[i]-1):
            root = i
            continue
        try:
            G[a[i]-1].append(i)
        except KeyError:
            G[a[i]-1] = [i]
    
    # print(G)
    paths = []
    bfs(root, a)
    print(len(paths))
    for p in paths:
        print(len(p))
        print(' '.join(map(lambda x: str(x+1), p)))
    print('')

