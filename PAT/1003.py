from queue import PriorityQueue
import itertools

def bfs(g, s):
    global d, path
    q = PriorityQueue()
    d[s] = 0
    q.put((d[s], s))
    

    while not q.empty():
        dis, u = q.get()
        for v, w in g[u]:
            if(d[u] + w <= d[v]):
                d[v] = d[u] + w
                path[v].append(u)
                q.put((d[v], v))


def dfs(g, u, t):
    global vis, count
    vis[u] = 1
    if(u == t):
        count += 1
        return
    for v in g[u]:
        dfs(g, v, t)

# main
n, m, s, t = map(int, input().split())
a = list(map(int, input().split()))

G = {}
path = {}
for i in range(n):
    G[i] = []
    path[i] = []

for i in range(m):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))


d = [0x3f3f3f3f]*n
bfs(G, t)
# print(d)
# print(path)

count = 0
vis = [0]*n
dfs(path, s, t)
# print(vis)
print(count, sum(itertools.compress(a, vis)))
