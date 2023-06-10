
def goto(v):
    print(v, flush=True)
    return list(map(int, input().split()))[1:]

def solve():
    n, m = map(int, input().split())
    G = [list() for _ in range(n+1)]
    vis = [0] * (n+1)
    pa = [-1] * (n+1)

    u = 1
    G[u] = list(map(int, input().split()))[1:]
    while u!=-1:
        vis[u] = 1
        for v in G[u]:
            if v == n:
                print(v, flush = True)
                return 
        flag = False
        for v in G[u]:
            if vis[v] == 0:
                G[v] = goto(v)
                pa[v] = u
                u = v
                flag = True
                break
        if not flag:
            u = pa[u]
            G[u] = goto(u)


solve()




