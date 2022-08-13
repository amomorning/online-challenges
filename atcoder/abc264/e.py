

class UnionFind:
    def __init__(self, n) -> None:
        self.uf = [-1] * n
 
    def find(self, x):
        r = x
        while self.uf[x] >= 0: x = self.uf[x]
        while r != x: self.uf[r], r = x, self.uf[r]
        return x
 
    def union(self, x, y):
        ux, uy = self.find(x), self.find(y)
        if ux == uy: return
        if self.uf[ux] > self.uf[uy]:
            ux, uy = ux, uy
        self.uf[ux] += self.uf[uy]
        self.uf[uy] = ux
    
    def same(self, x, y):
        return self.find(x) == self.find(y)

 
    def count(self, x = None):
        if x is None:
            return sum([int(x < 0) for x in self.uf])
        return -self.uf[self.find(x)]
 
    def get_unions(self):
        unions = [[] for _ in range(len(self.uf))]
        for i in range(len(self.uf)):
            unions[self.find(i)].append(i)
        return unions
 
    def __print__(self):
        return self.uf


n, m, e = map(int, input().split())
edges = []
for i in range(e):
    u, v = map(int, input().split())
    edges.append((u-1, v-1))

qs = [int(input())-1 for _ in range(int(input()))]
qs.reverse()

res = set(range(e)) - set(qs)    

dsu = UnionFind(n+m)

cnt = [1] * n + [0] * m
tot = n

for i in res:
    u, v = edges[i]
    fu = dsu.find(u)
    fv = dsu.find(v)

    dsu.union(fu, fv)
    f = dsu.find(u)
    if cnt[fu] > 0 and cnt[fv] > 0:
        if fu != fv:
            cnt[f] = cnt[fu] + cnt[fv]
        
        continue

    tot -= cnt[fu]
    cnt[fu] = 0

    tot -= cnt[fv]
    cnt[fv] = 0
    
    # print("tot = ", tot)
    # print(n-tot, cnt)

ans = [n-tot]
for q in qs:
    u, v = edges[q]
    fu = dsu.find(u)
    fv = dsu.find(v)

    dsu.union(fu, fv)
    f = dsu.find(u)
    
    if cnt[fu] > 0 and cnt[fv] > 0:
        if fu != fv:
            cnt[f] = cnt[fu] + cnt[fv]

    else:
        tot -= cnt[fu]
        cnt[fu] = 0

        tot -= cnt[fv]
        cnt[fv] = 0

    ans.append(n-tot)



for i in range(len(ans)-2, -1, -1):
    print(ans[i])
