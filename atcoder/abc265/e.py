import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
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
class Encodict:
    def __init__(self, func=lambda : 0):
        self.RANDOM = random.randint(0, 1<<32)
        self.default = func
        self.dict = {}
    
    def __getitem__(self, key):
        k = self.RANDOM ^ key
        if k not in self.dict:
            self.dict[k] = self.default()
        return self.dict[k]
    
    def __setitem__(self, key, item):
        k = self.RANDOM ^ key
        self.dict[k] = item

    def keys(self):
        return [self.RANDOM ^ i for i in self.dict]
    
    def items(self):
        return [(self.RANDOM ^ i, self.dict[i]) for i in self.dict]
    
    def sorted(self, by_value=False, reverse=False):
        if by_value:
            self.dict = dict(sorted(self.dict.items(), \
                key=lambda x:x[1], reverse=reverse))
        else:
            self.dict = dict(sorted(self.dict.items(), \
                key=lambda x:self.RANDOM^x[0], reverse=reverse))

def check(x, y, mp):
    lb = bisect.bisect_left(mp[x], y)
    if lb == len(mp[x]): return False
    if mp[x][lb] == y: return True
    return False

MOD = 998244353

n, m = inp()
A, B, C, D, E, F = inp()
mp = Encodict(list)
for i in range(m):
    x, y = inp()
    mp[x].append(y)

for x in mp.keys():
    mp[x] = sorted(mp[x])
# print(mp.items())
dp = [[[0] * (n+1) for _ in range(n+1)] for _ in range(n+1)]
dp[0][0][0] = 1
tot = 0
for i in range(n+1):
    for j in range(n-i+1):
        for k in range(n-i-j+1):
            # print(i, j, k)
            if dp[i][j][k] != 0:
                x, y = (i*A+j*C+k*E), (i*B+j*D+k*F)
                # print(x, y)
                if check(x, y, mp): 
                    dp[i][j][k] = 0
                    continue
                if i+j+k == n: 
                    # print(i, j, k, dp[i][j][k])
                    tot = (tot + dp[i][j][k]) % MOD
                    continue
                # print(i, j, k)
                
                dp[i+1][j][k] = (dp[i][j][k] + dp[i+1][j][k]) % MOD
                dp[i][j+1][k] = (dp[i][j][k] + dp[i][j+1][k]) % MOD
                dp[i][j][k+1] = (dp[i][j][k] + dp[i][j][k+1]) % MOD

# print(dp)
print(tot)
