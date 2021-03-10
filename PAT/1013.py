# tle at test 4
n, m, k = map(int, input().split())
G = {}
vis = [False]*n
for i in range(n):
    G[i] = []

for i in range(m):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)


def dfs(u):
    global vis
    vis[u] = 1
    for v in G[u]:
        if(not vis[v]):
            dfs(v)
    
    

qs = list(map(int, input().split()))
for q in qs:
    cnt = 0
    vis = [False]*(n)
    vis[q-1] = 1
    for i in range(n):
        if(not vis[i]):
            dfs(i)
            cnt += 1
            
    print(cnt-1)

