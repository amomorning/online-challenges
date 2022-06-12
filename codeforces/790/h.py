import sys;input=lambda:sys.stdin.readline().strip("\r\n")
import platform
LOCAL = (platform.uname().node == 'AMO')
# print(LOCAL)
def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)


class Fenwick:
    def __init__(self, n):
        
        self.n = n
        self.bits = [0] * (n+1)
    
    def sum(self, i):
        ret = 0
        while i > 0:
            ret += self.bits[i]
            i -= i & -i
        return ret
    
    def add(self, i, x):
        while i <= self.n:
            self.bits[i] += x
            i += i & -i


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()

    fenwick = Fenwick(n)
    res = 0
    for i, x in enumerate(a):
        res += fenwick.sum(x)
        fenwick.add(x, 1)
        # printf(res)
    printf(res)


        
