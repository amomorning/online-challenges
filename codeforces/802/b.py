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
input = lambda: sys.stdin.readline().rstrip("\r\n")


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


def minus(a, b):
    n = len(b)
    delta = 0
    if len(a) > len(b):
        delta = 1

    remain = 0
    ans = ''
    for i in range(n-1, -1, -1):
        left = int(a[i + delta]) - remain
        right = int(b[i])

        if left < right:
            left += 10
            remain = 1 
        else:
            remain = 0
        ans = str(left - right) + ans
        # debug(ans)
    return ans
        

        

for _ in range(int(input())):
    n = int(input())
    s = input()

    if n < 5:
        ans = int('1' + '0'*(n-1) + '1') - int(s)
        if len(str(ans)) < n:
            ans = int('1' + '1'*(n-1) + '1') - int(s)

        printf(ans)
        continue


    first = int(s[:2]) + 11

    tmp = str(first)
    if first > 99:
        lst = tmp + '0'* (n-5) + tmp[::-1]
    else:
        lst = tmp + '0'* (n-4) + tmp[::-1]

    # debug(lst)
    # debug(int(minus(lst, s)) + int(s))
    printf(minus(lst, s))
    
