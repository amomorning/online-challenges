import collections, math, bisect, heapq, random, functools, itertools, copy
import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printt(a):
    if LOCAL:
        printf(a)

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)



class RandomDict:
    def __init__(self, func=lambda x: 0):
        self.RANDOM = random.randint(0, 1<<32)
        self.default = func
        self.dict = {}
    
    def __getitem__(self, key):
        k = self.RANDOM ^ key
        if k not in self.dict:
            self.dict[k] = self.default()
        return self.dict[k]
    
    def __setitem__(self, key, value):
        k = self.RANDOM ^ key
        self.dict[k] = value

    def keys(self):
        return [self.RANDOM ^ i for i in self.dict]

from math import inf

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mp = RandomDict(list)
    for i in range(n):
        mp[a[i]].append(i)
    
    ans = (-inf, -1, -1, -1)
    for k in mp.keys():
        s = (inf, -1)
        m = len(mp[k])

        for i in range(m-1, -1, -1):
            p = mp[k][i]
            s = min(s, (m-i-(n-p-(m-i)), p))
            ans = max(ans, (m-i-(n-p-(m-i))-s[0], k, p, s[1]))

    print(ans[1], ans[2]+1, ans[3]+1)

    