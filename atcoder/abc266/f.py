class UnionFind:
    def __init__(self, x) -> None:
        self.uf = [-1] * x
 
    def find(self, x):
        r = x
        while self.uf[x] >= 0:
            x = self.uf[x]
 
        while r != x:
            self.uf[r], r = x, self.uf[r]
        return x
 
    def union(self, x, y):
        ux, uy = self.find(x), self.find(y)
        if ux == uy:
            return
        if self.uf[ux] >= self.uf[uy]:
            self.uf[uy] += self.uf[ux]
            self.uf[ux] = uy
        else:
            self.uf[ux] += self.uf[uy]
            self.uf[uy] = ux
        return

    
    def same(self, x, y):
        ux, uy = self.find(x), self.find(y)
        return ux == uy
 
    def count(self):
        ans = 0
        for c in self.uf:
            if c < 0:
                ans += 1
        return ans
 
    def valid(self):
        n = len(self.uf)
        for c in range(n):
            if self.uf[c] == -n:
                return True
        return False
 
    def __print__(self):
        return self.uf

from collections import deque
def bfs(u, ring):
    pre = [-1] * N
    q = deque()
    q.append(u)
    while q:
        u = q.popleft()
        for v in G[u]:
            if v == pre[u]: continue
            if pre[v] == -1:
                q.append(v) 
                pre[v] = u
            else:
                a = set()
                while u != -1:
                    a.add(u)
                    u = pre[u]
                while v != -1:
                    ring.add(v)
                    if v in a:
                        vv = v
                        break
                    v = pre[v]
                for x in a:
                    if x == vv:
                        break
                    ring.add(x)
                    
                return


N = int(input())
G = [[] for _ in range(N)]
for i in range(N):
    u, v = map(int, input().split()); u -= 1; v -= 1
    G[u].append(v)
    G[v].append(u)

ring = set()
bfs(0, ring)
# print(ring)
dsu = UnionFind(N)
vis = [0] * N
for u in ring:
    vis[u] = 1
    for v in G[u]:
        if v not in ring:
            # print(u, v, G[u])
            dsu.union(u, v)
            q = deque()
            q.append(v)
            while q:
                uu = q.popleft()
                vis[uu] = 1
                dsu.union(uu, v)
                for vv in G[uu]:
                    if vis[vv] != 1:
                        q.append(vv)
        
                        
# print(dsu.uf)
                    
Q = int(input())
for _ in range(Q):
    u, v = map(int, input().split()); u -= 1; v -= 1
    if dsu.same(u, v):
        print("Yes")
    else:
        print("No")
