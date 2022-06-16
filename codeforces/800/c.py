import collections, math, bisect, heapq, random, functools, itertools, copy, typing
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
input = lambda: sys.stdin.readline().rstrip("\r\n")


def debug(*args):
    print('\033[92m', end='', file=sys.stderr)
    print(*args, file=sys.stderr, end='')
    print('\033[0m', file=sys.stderr)

def printf(*args):
    for arg in args:
        if isinstance(arg, typing.Iterable):
            print(' '.join(map(str, arg)), end=' ')
        else:
            print(arg, end=' ')
    print()

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    flag = True
    now = n-1

    while now > 0 and a[now] == 0:
        now -= 1
    
    cur = 0
    for i in range(now, 0, -1):
        cur += a[i]
        if cur >= 0:
            flag = False
    cur += a[0]
    if cur != 0:
        flag = False
        
    print("YES") if flag == True else print("NO")
