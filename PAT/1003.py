from queue import PriorityQueue
import itertools


def bfs(g, s):
    global d, num, a, weight
    q = PriorityQueue()
    d[s] = 0
    q.put((d[s], s))
    num[s] = 1
    weight[s] = a[s]

    while not q.empty():
        dis, u = q.get()
        for v, w in g[u]:
            if(d[u] + w < d[v]):
                d[v] = d[u] + w
                q.put((d[v], v))

                num[v] = num[u]
                weight[v] = weight[u] + a[v]
            elif(d[u] + w == d[v]):
                num[v] = num[v] + num[u]
                if(weight[u] + a[v] > weight[v]):
                    weight[v] = weight[u] + a[v]


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
weight, num = [0]*n, [0]*n
bfs(G, t)


print(num[s], weight[s])
