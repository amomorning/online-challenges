import sys; input = lambda:sys.stdin.readline().strip("\r\n")

class SparseTable:
    def __init__(self, a, select=min):
        n = len(a); L = 1
        while (1 << L) <= n: L += 1

        self.lg = [-1] * (n + 1)
        self.u = [[0] * (L+1) for _ in range(n)]
        self.select = select

        for i in range(n):
            self.u[i][0] = a[i]
        for i in range(1, n + 1):
            self.lg[i] = self.lg[i >> 1] + 1
        for j in range(1, L):
            for i in range(n-(1<<j)+1):
                self.u[i][j] = self.select(self.u[i][j - 1], self.u[i + (1 << (j - 1))][j - 1])
        
    def ask(self, a, b):
        k = self.lg[b-a+1]
        return self.select(self.u[a][k], self.u[b - (1 << k) + 1][k])

import math
n, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

diffa = []
for i in range(1, n):
    diffa.append(abs(a[i] - a[i-1]))

diffb = []
for i in range(1, n):
    diffb.append(abs(b[i] - b[i-1]))

sta = SparseTable(diffa, math.gcd)
stb = SparseTable(diffb, math.gcd)

for _ in range(q):
    h1, h2, w1, w2 = map(int, input().split())
    ans = a[h1-1] + b[w1-1]
    if h1 != h2:
        ans = math.gcd(ans, sta.ask(h1-1, h2-2))
    if w1 != w2:
        ans = math.gcd(ans, stb.ask(w1-1, w2-2))

    print(ans)
