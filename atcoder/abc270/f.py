import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')

# Fast IO Region
import os, sys; from io import BytesIO, IOBase
BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
inp = lambda : list(map(int, input().split()))

def debug(*args):
    if LOCAL:
        print('\033[92m', end='')
        printf(*args)
        print('\033[0m', end='')

def printf(*args):
    if LOCAL:
        print('>>>: ', end='')
    for arg in args:
        if isinstance(arg, typing.Iterable) and \
                not isinstance(arg, str) and \
                not isinstance(arg, dict):
            print(' '.join(map(str, arg)), end=' ')
        else:
            print(arg, end=' ')
    print()

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
 
    def same(self, x, y):
        return self.find(x) == self.find(y)

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

def bit_count(x):
    return bin(x).count('1')

N, M = inp()
X = inp()
Y = inp()
edges = []
G = [[] for _ in range(N)]
for i in range(M):
    A, B, Z = inp()
    A -= 1; B -= 1
    edges.append((Z, A, B, 0))

for i in range(N):
    edges.append((X[i], i, N, 1))
    edges.append((Y[i], i, N+1, 2))

edges = sorted(edges, key=lambda x: x[0])
ans = math.inf

for t in range(4):
    # print(es)
    uf = UnionFind(N + bit_count(t))

    tot, num = 0, 0
    for w, u, v, op in edges:
        if op == 0 or (t & (1<<(op-1))):
            if t == 2 and op == 2:
                v -= 1
            if uf.same(u, v): continue
            tot += w
            num += 1
            uf.union(u, v)
            if num == N + bit_count(t) - 1:
                break
    if num == N + bit_count(t) - 1:
        ans = min(ans, tot)

print(ans)
