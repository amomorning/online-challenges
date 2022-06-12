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

import bisect

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    mp = {}
    for i in range(n):
        mp[a[i]] = 0
    for i in range(n):
        mp[a[i]] += 1
    keys = sorted(mp.keys())
    lenk = len(keys)

    tot = 0
    cur = 0
    for i in range(lenk):
        k = keys[i]

        if(mp[k] > 1):
            tot += 1
        else:
            if(cur == 1):
                tot += 1
            cur ^= 1

    if cur == 1:
        tot += 1

    printf(tot)
 
