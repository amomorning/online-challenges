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

import heapq

q = int(input())
mp = {}
mx = []
mn = []
for _ in range(q):
    op, *a = map(int, input().split())
    if op == 1:
        if a[0] in mp:
            mp[a[0]] += 1
        else:
            mp[a[0]] = 1
        heapq.heappush(mx, -a[0])
        heapq.heappush(mn, a[0])
    elif op == 2:
        x, c = a
        if x in mp:
            mp[x] -= min(mp[x], c)

    elif op == 3:
        u, v = mx[0], mn[0]

        # printf([u, v])
        while mp[-u] == 0:
            heapq.heappop(mx)
            u = mx[0]
        while mp[v] == 0:
            heapq.heappop(mn)
            v = mn[0]

        printf(-u - v)
            

