from re import A, S
import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

from bisect import bisect_left
from math import inf

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(-1)

    cur = [0, a[0], 1]
    trains = []
    for i in range(1, n+1):
        trains.append((i, a[i], 1))
        # if a[i] >= cur[1]:
        #     cur[2] += 1
        # else:
        #     trains.append(tuple(cur))
        #     cur = [i, a[i], 1]
        
    res = []
    for q in range(m):
        k, d = map(int, input().split()); k-=1

        id = bisect_left(trains, (k, inf, inf)) - 1
        cur = list(trains[id])
        printf(cur)
        del trains[id]
        now = id + 1
        if k != cur[0]:
            now += 1
            trains.insert(id, (cur[0], cur[1], k-cur[0]))

        cur = [k, cur[1]-d, cur[2]-(k-cur[0])]
        bound = len(trains)

        while now < bound and trains[now][1] >= cur[1]:
            cur[2] += trains[now][2]
            del trains[now]
            bound -= 1
            now += 1
        trains.insert(id+1, tuple(cur))
        
        printf(trains)
        res.append(len(trains))
        
    printf(res)
    