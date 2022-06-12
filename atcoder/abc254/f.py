import sys; input = lambda:sys.stdin.readline().strip("\r\n")

class SparseTable:
    def __init__(self, a, select=min):
        N = len(a); 
        L = N.bit_length()

        self.u = [[0] * N for _ in range(L)]
        self.select = select

        for i in range(N):
            self.u[0][i] = a[i]
        for i in range(1, L):
            for j in range(N-(1<<i)+1):
                self.u[i][j] = self.select(self.u[i-1][j], self.u[i-1][j+(1<<(i-1))])
        
    def ask(self, l, r):
        i = (r - l).bit_length()-1
        return self.select(self.u[i][l], self.u[i][r-(1<<i)+1])


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
