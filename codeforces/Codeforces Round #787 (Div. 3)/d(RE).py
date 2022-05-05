t = int(input())

path = []
vis = []
layer = {}
G = {}

def get_layer(u, depth):
    global layer
    try:
        layer[depth].append(u)
    except KeyError:
        layer[depth] = [u]
    
    if(u not in G):
        return 
    for v in G[u]:
        get_layer(v, depth+1)

def dfs(u):
    global path
    global vis
    path.append(u)
    vis[u] = 1

    if(u not in G):
        return

    for v in G[u]:
        if(vis[v] == 0):
            dfs(v)
            break



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

    layer = {}
    # print(G)
    get_layer(root, 0)

    # print(layer)

    vis = [0] * n
    paths = []

    for i in layer:
        for u in layer[i]:
            if(vis[u] == 0):
                path = []
                
                dfs(u)
                paths.append(path)

    print(len(paths))
    for p in paths:
        print(len(p))
        print(' '.join(map(lambda x: str(x+1), p)))
    print('')


